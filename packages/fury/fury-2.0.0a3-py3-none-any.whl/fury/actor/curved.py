"""Curved primitives actors."""

from concurrent.futures import ThreadPoolExecutor

import numpy as np

from fury.actor import actor_from_primitive
from fury.geometry import buffer_to_geometry, create_mesh, line_buffer_separator
from fury.lib import Line, register_wgpu_render_function
from fury.material import StreamlinesMaterial, _create_mesh_material, validate_opacity
from fury.optpkg import optional_package
import fury.primitive as fp
from fury.shader import StreamlinesShader

numba, have_numba, _ = optional_package("numba")

# Create a conditional numba decorator
if have_numba:
    njit = numba.njit
else:
    # No-op decorator when numba is not available
    def njit(*args, **kwargs):
        def decorator(func):
            return func

        return decorator


def sphere(
    centers,
    *,
    colors=(1, 0, 0),
    radii=1.0,
    phi=16,
    theta=16,
    opacity=None,
    material="phong",
    enable_picking=True,
    smooth=True,
):
    """Create one or many spheres with different colors and radii.

    Parameters
    ----------
    centers : ndarray, shape (N, 3)
        Spheres positions.
    colors : ndarray, shape (N, 3) or (N, 4) or tuple (3,) or tuple (4,), optional
        RGB or RGBA (for opacity) R, G, B, and A should be in the range [0, 1].
    radii : float or ndarray, shape (N,), optional
        Sphere radius. Can be a single value for all spheres or an array of
        radii for each sphere.
    phi : int, optional
        The number of segments in the longitude direction.
    theta : int, optional
        The number of segments in the latitude direction.
    opacity : float, optional
        Takes values from 0 (fully transparent) to 1 (opaque).
        If both `opacity` and RGBA are provided, the final alpha will be:
        final_alpha = alpha_in_RGBA * opacity.
    material : str, optional
        The material type for the spheres. Options are 'phong' and 'basic'.
    enable_picking : bool, optional
        Whether the spheres should be pickable in a 3D scene.
    smooth : bool, optional
        Whether to create a smooth sphere or a faceted sphere.

    Returns
    -------
    Actor
        A mesh actor containing the generated spheres, with the specified
        material and properties.

    Examples
    --------
    >>> from fury import window, actor
    >>> import numpy as np
    >>> scene = window.Scene()
    >>> centers = np.random.rand(5, 3) * 10
    >>> colors = np.random.rand(5, 3)
    >>> radii = np.random.rand(5)
    >>> sphere_actor = actor.sphere(centers=centers, colors=colors, radii=radii)
    >>> _ = scene.add(sphere_actor)
    >>> show_manager = window.ShowManager(scene=scene, size=(600, 600))
    >>> show_manager.start()
    """

    scales = radii
    directions = (1, 0, 0)

    vertices, faces = fp.prim_sphere(phi=phi, theta=theta)
    return actor_from_primitive(
        vertices,
        faces,
        centers=centers,
        colors=colors,
        scales=scales,
        directions=directions,
        opacity=opacity,
        material=material,
        smooth=smooth,
        enable_picking=enable_picking,
    )


def ellipsoid(
    centers,
    *,
    orientation_matrices=None,
    lengths=(4, 2, 2),
    colors=(1, 0, 0),
    opacity=None,
    phi=16,
    theta=16,
    material="phong",
    enable_picking=True,
    smooth=True,
):
    """
    Create ellipsoid actor(s) with specified orientation and scaling.

    Parameters
    ----------
    centers : ndarray (N, 3)
        Centers of the ellipsoids.
    orientation_matrices : ndarray, shape (N, 3, 3) or (3, 3), optional
        Orthonormal rotation matrices defining the orientation of each ellipsoid.
        Each 3×3 matrix represents a local coordinate frame, with columns
        corresponding to the ellipsoid’s x-, y-, and z-axes in world coordinates.
        Must be right-handed and orthonormal. If a single (3, 3) matrix is
        provided, it is broadcast to all ellipsoids.
    lengths : ndarray (N, 3) or (3,) or tuple (3,), optional
        Scaling factors along each axis.
    colors : array-like or tuple, optional
        RGB/RGBA colors for each ellipsoid.
    opacity : float, optional
        Opacity of the ellipsoids. Takes values from 0 (fully transparent) to
        1 (opaque). If both `opacity` and RGBA are provided, the final alpha
        will be: final_alpha = alpha_in_RGBA * opacity.
    phi : int, optional
        The number of segments in the longitude direction.
    theta : int, optional
        The number of segments in the latitude direction.
    material : str, optional
        The material type for the ellipsoids. Options are 'phong' and 'basic'.
    enable_picking : bool, optional
        Allow picking of the ellipsoids in a 3D scene.
    smooth : bool, optional
        Whether to create a smooth ellipsoid or a faceted ellipsoid.

    Returns
    -------
    Actor
        A mesh actor containing the generated ellipsoids.

    Examples
    --------
    >>> from fury import window, actor
    >>> import numpy as np
    >>> from fury import actor, window
    >>> centers = np.array([[0, 0, 0]])
    >>> lengths = np.array([[2, 1, 1]])
    >>> colors = np.array([[1, 0, 0]])
    >>> ellipsoid = actor.ellipsoid(centers=centers, lengths=lengths, colors=colors)
    >>> window.show([ellipsoid])
    """

    centers = np.asarray(centers)

    if orientation_matrices is None:
        orientation_matrices = np.tile(np.eye(3), (centers.shape[0], 1, 1))

    orientation_matrices = np.asarray(orientation_matrices)
    lengths = np.asarray(lengths)
    colors = np.asarray(colors)

    if centers.ndim == 1:
        centers = centers.reshape(1, 3)
    if centers.ndim != 2 or centers.shape[1] != 3:
        raise ValueError("Centers must be (N, 3) array")
    if orientation_matrices.ndim == 2:
        orientation_matrices = np.tile(orientation_matrices, (centers.shape[0], 1, 1))
    if orientation_matrices.ndim != 3 or orientation_matrices.shape[1:] != (3, 3):
        raise ValueError("Axes must be (N, 3, 3) array")
    if lengths.ndim == 1:
        lengths = lengths.reshape(1, 3)
    if lengths.ndim != 2 or lengths.shape[1] != 3:
        raise ValueError("Lengths must be (N, 3) array")
    if lengths.size == 3:
        lengths = np.tile(lengths.reshape(1, -1), (centers.shape[0], 1))
    if lengths.shape != centers.shape:
        raise ValueError("Lengths must match centers shape")
    if colors.size == 3 or colors.size == 4:
        colors = np.tile(colors.reshape(1, -1), (centers.shape[0], 1))

    base_verts, base_faces = fp.prim_sphere(phi=phi, theta=theta)

    base_verts = np.asarray(base_verts)
    base_faces = np.asarray(base_faces)

    if base_verts.ndim != 2 or base_verts.shape[1] != 3:
        raise ValueError(f"base_verts has unexpected shape {base_verts.shape}")

    if isinstance(colors, (list, tuple)):
        colors = np.asarray(colors)
        if colors.ndim == 1:
            colors = np.tile(colors, (centers.shape[0], 1))

    n_ellipsoids = centers.shape[0]
    n_verts = base_verts.shape[0]

    scaled_transforms = orientation_matrices * lengths[:, np.newaxis, :]

    transformed = (
        np.einsum("nij,mj->nmi", scaled_transforms, base_verts)
        + centers[:, np.newaxis, :]
    )
    all_vertices = transformed.reshape(-1, 3)
    all_faces = np.tile(base_faces, (n_ellipsoids, 1)) + (
        np.arange(n_ellipsoids)[:, None, None] * n_verts
    )
    all_faces = all_faces.reshape(-1, 3)
    all_colors = np.repeat(colors, n_verts, axis=0)

    return actor_from_primitive(
        centers=centers,
        vertices=all_vertices,
        faces=all_faces,
        colors=all_colors,
        opacity=opacity,
        material=material,
        smooth=smooth,
        enable_picking=enable_picking,
        repeat_primitive=False,
    )


def cylinder(
    centers,
    *,
    colors=(1, 1, 1),
    height=1,
    sectors=36,
    radii=0.5,
    scales=(1, 1, 1),
    directions=(0, 1, 0),
    capped=True,
    opacity=None,
    material="phong",
    enable_picking=True,
):
    """Create one or many cylinders with different features.

    Parameters
    ----------
    centers : ndarray, shape (N, 3)
        Cylinder positions.
    colors : ndarray, shape (N, 3) or (N, 4) or tuple (3,) or tuple (4,), optional
        RGB or RGBA (for opacity) R, G, B, and A should be in the range [0, 1].
    height : float, optional
        The height of the cylinder.
    sectors : int, optional
        The number of divisions around the cylinder's circumference.
        Higher values produce smoother cylinders.
    radii : float or ndarray, shape (N,) or tuple, optional
        The radius of the base of the cylinders. A single value applies to all
        cylinders,
        while an array specifies a radius for each cylinder individually.
    scales : ndarray, shape (N, 3) or tuple (3,) or float, optional
        The size of the cylinder in each dimension. If a single value is provided,
        the same size will be used for all cylinders.
    directions : ndarray, shape (N, 3) or tuple (3,), optional
        The orientation vector of the cylinder.
    capped : bool, optional
        Whether to add caps (circular ends) to the cylinders.
    opacity : float, optional
        Takes values from 0 (fully transparent) to 1 (opaque).
        If both `opacity` and RGBA are provided, the final alpha will be:
        final_alpha = alpha_in_RGBA * opacity.
    material : str, optional
        The material type for the cylinders. Options are 'phong' and 'basic'.
    enable_picking : bool, optional
        Whether the cylinders should be pickable in a 3D scene.

    Returns
    -------
    Actor
        A mesh actor containing the generated cylinders, with the specified
        material and properties.

    Examples
    --------
    >>> from fury import window, actor
    >>> import numpy as np
    >>> scene = window.Scene()
    >>> centers = np.random.rand(5, 3) * 10
    >>> colors = np.random.rand(5, 3)
    >>> cylinder_actor = actor.cylinder(centers=centers, colors=colors)
    >>> _ = scene.add(cylinder_actor)
    >>> show_manager = window.ShowManager(scene=scene, size=(600, 600))
    >>> show_manager.start()
    """

    vertices, faces = fp.prim_cylinder(
        radius=radii, height=height, sectors=sectors, capped=capped
    )
    return actor_from_primitive(
        vertices,
        faces,
        centers=centers,
        colors=colors,
        scales=scales,
        directions=directions,
        opacity=opacity,
        material=material,
        enable_picking=enable_picking,
    )


def cone(
    centers,
    *,
    colors=(1, 1, 1),
    height=1,
    sectors=10,
    radii=0.5,
    scales=(1, 1, 1),
    directions=(0, 1, 0),
    opacity=None,
    material="phong",
    enable_picking=True,
):
    """Create one or many cones with different features.

    Parameters
    ----------
    centers : ndarray, shape (N, 3)
        Cone positions.
    colors : ndarray, shape (N, 3) or (N, 4) or tuple (3,) or tuple (4,), optional
        RGB or RGBA (for opacity) R, G, B, and A should be in the range [0, 1].
    height : float, optional
        The height of the cone.
    sectors : int, optional
        The number of divisions around the cone's circumference.
        Higher values produce smoother cones.
    radii : float or ndarray, shape (N,) or tuple, optional
        The radius of the base of the cones. A single value applies to all cones,
        while an array specifies a radius for each cone individually.
    scales : ndarray, shape (N, 3) or tuple (3,) or float, optional
        The size of the cone in each dimension. If a single value is provided,
        the same size will be used for all cones.
    directions : ndarray, shape (N, 3) or tuple (3,), optional
        The orientation vector of the cone.
    opacity : float, optional
        Takes values from 0 (fully transparent) to 1 (opaque).
        If both `opacity` and RGBA are provided, the final alpha will be:
        final_alpha = alpha_in_RGBA * opacity.
    material : str, optional
        The material type for the cones. Options are 'phong' and 'basic'.
    enable_picking : bool, optional
        Whether the cones should be pickable in a 3D scene.

    Returns
    -------
    Actor
        A mesh actor containing the generated cones, with the specified
        material and properties.

    Examples
    --------
    >>> from fury import window, actor
    >>> import numpy as np
    >>> scene = window.Scene()
    >>> centers = np.random.rand(5, 3) * 10
    >>> colors = np.random.rand(5, 3)
    >>> cone_actor = actor.cone(centers=centers, colors=colors)
    >>> _ = scene.add(cone_actor)
    >>> show_manager = window.ShowManager(scene=scene, size=(600, 600))
    >>> show_manager.start()
    """

    vertices, faces = fp.prim_cone(radius=radii, height=height, sectors=sectors)
    return actor_from_primitive(
        vertices,
        faces,
        centers=centers,
        colors=colors,
        scales=scales,
        directions=directions,
        opacity=opacity,
        material=material,
        enable_picking=enable_picking,
    )


class Streamlines(Line):
    """
    Create a streamline representation.

    Parameters
    ----------
    lines : ndarray, shape (N, 3)
        The positions of the points along the streamline.
    colors : ndarray, shape (N, 3) or (N, 4), optional
        RGB or RGBA (for opacity) R, G, B and A should be at the range [0, 1].
    thickness : float, optional
        The thickness of the streamline.
    opacity : float, optional
        The opacity of the streamline.
    outline_thickness : float, optional
        The thickness of the outline.
    outline_color : tuple, optional
        The color of the outline.
    enable_picking : bool, optional
        Whether the streamline should be pickable in a 3D scene, by default True.
    """

    def __init__(
        self,
        lines,
        *,
        colors=None,
        thickness=2.0,
        opacity=1.0,
        outline_thickness=1.0,
        outline_color=(1, 0, 0),
        enable_picking=True,
    ):
        """
        Create a streamline representation.

        Parameters
        ----------
        lines : ndarray, shape (N, 3)
            The positions of the points along the streamline.
        colors : ndarray, shape (N, 3) or (N, 4), optional
            RGB or RGBA (for opacity) R, G, B and A should be at the range [0, 1].
        thickness : float, optional
            The thickness of the streamline.
        opacity : float, optional
            The opacity of the streamline.
        outline_thickness : float, optional
            The thickness of the outline.
        outline_color : tuple, optional
            The color of the outline.
        enable_picking : bool, optional
            Whether the streamline should be pickable in a 3D scene.

        Raises
        ------
        ValueError
            If lines is not a valid numpy array with shape (N, 3).
        ValueError
            If colors is not a valid color tuple or array.
        ValueError
            If thickness or outline_thickness is not a positive number.
        ValueError
            If opacity is not between 0 and 1.
        TypeError
            If enable_picking is not a boolean.
        """
        super().__init__()

        if not isinstance(thickness, (int, float)) or thickness <= 0:
            raise ValueError("thickness must be a positive number")

        opacity = validate_opacity(opacity)

        if not isinstance(outline_thickness, (int, float)) or outline_thickness < 0:
            raise ValueError("outline_thickness must be a non-negative number")

        outline_color = np.asarray(outline_color, dtype=np.float32)
        if outline_color.size not in (3, 4):
            raise ValueError(
                "outline_color must be a tuple/array of 3 (RGB) or 4 (RGBA) values"
            )
        if not np.all((outline_color >= 0) & (outline_color <= 1)):
            raise ValueError("outline_color values must be between 0 and 1")

        if not isinstance(enable_picking, bool):
            raise TypeError("enable_picking must be a boolean")

        self.geometry = buffer_to_geometry(
            positions=lines.astype("float32"), colors=colors.astype("float32")
        )

        self.material = StreamlinesMaterial(
            outline_thickness=outline_thickness,
            outline_color=outline_color,
            pick_write=enable_picking,
            opacity=opacity,
            thickness=thickness,
            color_mode="vertex",
        )


def streamlines(
    lines,
    *,
    colors=(1, 0, 0),
    thickness=2.0,
    opacity=1.0,
    outline_thickness=1.0,
    outline_color=(0, 0, 0),
    enable_picking=True,
):
    """Create a streamline representation.

    Parameters
    ----------
    lines : list of ndarray of shape (P, 3) or ndarray of shape (N, P, 3)
        Lines points.
    colors : ndarray, shape (N, 3) or (N, 4) or tuple (3,) or tuple (4,), optional
        RGB or RGBA (for opacity) R, G, B and A should be at the range [0, 1].
    thickness : float, optional
        The thickness of the streamline.
    opacity : float, optional
        The opacity of the streamline.
    outline_thickness : float, optional
        The thickness of the outline.
    outline_color : tuple, optional
        The color of the outline.
    enable_picking : bool, optional
        Whether the streamline should be pickable in a 3D scene.

    Returns
    -------
    Streamline
        The created streamline object.
    """
    lines_positions, lines_colors = line_buffer_separator(lines, color=colors)

    return Streamlines(
        lines_positions,
        colors=lines_colors,
        thickness=thickness,
        opacity=opacity,
        outline_thickness=outline_thickness,
        outline_color=outline_color,
        enable_picking=enable_picking,
    )


@register_wgpu_render_function(Streamlines, StreamlinesMaterial)
def register_render_streamline(wobject):
    """Register the streamline render function.

    Parameters
    ----------
    wobject : Streamline
        The streamline object to register.

    Returns
    -------
    StreamlineShader
        The created streamline shader.
    """
    return StreamlinesShader(wobject)


@njit(cache=True)
def compute_tangents(points):
    """
    Calculate normalized tangent vectors for a series of points.

    Uses central differences for interior points and forward/backward for endpoints.

    Parameters
    ----------
    points : ndarray, shape (N, 3)
        Input points for which to compute tangents.

    Returns
    -------
    ndarray, shape (N, 3)
        Normalized tangent vectors for the input points.
    """
    N = points.shape[0]
    tangents = np.zeros_like(points)
    if N < 2:
        return tangents

    # Central difference for interior points
    for i in range(1, N - 1):
        tangents[i] = points[i + 1] - points[i - 1]

    # Forward/backward difference for endpoints
    tangents[0] = points[1] - points[0]
    tangents[-1] = points[-1] - points[-2]

    for i in range(N):
        norm = np.sqrt(np.sum(tangents[i] ** 2))
        if norm > 1e-6:
            tangents[i] /= norm
    return tangents


@njit(cache=True)
def parallel_transport_frames(tangents):
    """Generate a continuous coordinate frame along a curve defined by tangents.

    This is a continuous, non-twisting coordinate frame (normal, binormal)
    along a curve defined by tangents using parallel transport.

    Parameters
    ----------
    tangents : ndarray, shape (N, 3)
        Tangent vectors along the curve.

    Returns
    -------
    normals : ndarray, shape (N, 3)
        Normal vectors for the curve.
    binormals : ndarray, shape (N, 3)
        Binormal vectors for the curve.
    """
    N = tangents.shape[0]
    normals = np.zeros_like(tangents)
    binormals = np.zeros_like(tangents)
    if N == 0:
        return normals, binormals

    t0 = tangents[0]
    ref1 = np.array([0.0, 0.0, 1.0], dtype=tangents.dtype)
    ref2 = np.array([1.0, 0.0, 0.0], dtype=tangents.dtype)
    ref = ref1 if np.abs(np.dot(t0, ref1)) < 0.99 else ref2
    b0 = np.cross(t0, ref)
    b0_norm = np.linalg.norm(b0)
    if b0_norm > 1e-6:
        b0 /= b0_norm
    n0 = np.cross(b0, t0)
    n0_norm = np.linalg.norm(n0)
    if n0_norm > 1e-6:
        n0 /= n0_norm

    normals[0] = n0
    binormals[0] = b0

    for i in range(1, N):
        prev_t = tangents[i - 1]
        curr_t = tangents[i]
        axis = np.cross(prev_t, curr_t)
        sin_angle = np.linalg.norm(axis)
        cos_angle = np.dot(prev_t, curr_t)

        if sin_angle > 1e-6:
            axis /= sin_angle

            prev_n = normals[i - 1]
            normals[i] = (
                prev_n * cos_angle
                + np.cross(axis, prev_n) * sin_angle
                + axis * np.dot(axis, prev_n) * (1 - cos_angle)
            )
            prev_b = binormals[i - 1]
            binormals[i] = (
                prev_b * cos_angle
                + np.cross(axis, prev_b) * sin_angle
                + axis * np.dot(axis, prev_b) * (1 - cos_angle)
            )
        else:
            normals[i] = normals[i - 1]
            binormals[i] = binormals[i - 1]

    return normals, binormals


@njit(cache=True)
def generate_tube_geometry(points, number_of_sides, radius, end_caps):
    """Generate vertices and triangles for a single tube.

    This function is Core Numba-optimized function to generate vertices and triangles
    for a single tube.

    Parameters
    ----------
    points : ndarray, shape (N, 3)
        The points defining the centerline of the tube.
    number_of_sides : int
        The number of sides for the tube's cross-section.
    radius : float
        The radius of the tube.
    end_caps : bool
        Whether to include end caps on the tube.

    Returns
    -------
    vertices : ndarray, shape (V, 3)
        The vertices of the tube.
    indices : ndarray, shape (T, 3)
        The triangle indices for the tube.
    """
    N = points.shape[0]
    if N < 2:
        return np.zeros((0, 3), dtype=np.float32), np.zeros((0, 3), dtype=np.int32)

    tangents = compute_tangents(points)
    normals, binormals = parallel_transport_frames(tangents)

    cap_v_count = 2 if end_caps else 0
    total_vertices = N * number_of_sides + cap_v_count
    vertices = np.empty((total_vertices, 3), dtype=np.float32)

    num_tube_tris = (N - 1) * number_of_sides * 2
    cap_tri_count = number_of_sides * 2 if end_caps else 0
    indices = np.empty((num_tube_tris + cap_tri_count, 3), dtype=np.int32)

    step = (2 * np.pi) / number_of_sides
    angles = np.arange(number_of_sides) * step

    for i in range(N):
        for j in range(number_of_sides):
            offset = normals[i] * np.cos(angles[j]) + binormals[i] * np.sin(angles[j])
            vertices[i * number_of_sides + j] = points[i] + radius * offset

    idx = 0
    for i in range(N - 1):
        for j in range(number_of_sides):
            v1 = i * number_of_sides + j
            v2 = i * number_of_sides + (j + 1) % number_of_sides
            v3 = (i + 1) * number_of_sides + j
            v4 = (i + 1) * number_of_sides + (j + 1) % number_of_sides
            indices[idx] = [v1, v2, v4]
            indices[idx + 1] = [v1, v4, v3]
            idx += 2

    if end_caps:
        start_cap_v_idx = N * number_of_sides
        end_cap_v_idx = start_cap_v_idx + 1
        vertices[start_cap_v_idx] = points[0]
        vertices[end_cap_v_idx] = points[-1]

        for i in range(number_of_sides):
            indices[idx] = [(i + 1) % number_of_sides, i, start_cap_v_idx]
            idx += 1
            v_start_of_end_ring = (N - 1) * number_of_sides
            indices[idx] = [
                v_start_of_end_ring + i,
                v_start_of_end_ring + (i + 1) % number_of_sides,
                end_cap_v_idx,
            ]
            idx += 1
    return vertices, indices


def streamtube(
    lines,
    *,
    opacity=1.0,
    colors=(1, 1, 1),
    radius=0.2,
    segments=8,
    end_caps=True,
    flat_shading=False,
    material="phong",
    enable_picking=True,
):
    """
    Create a streamtube from a list of lines using parallel processing.

    Parameters
    ----------
    lines : list of ndarray, shape (N, 3)
        List of lines, where each line is a set of 3D points.
    opacity : float, optional
        Overall opacity of the actor, from 0.0 to 1.0.
    colors : tuple or ndarray, optional
        - A single color tuple (e.g., (1,0,0)) for all lines.
        - An array of colors, one for each line (e.g., [[1,0,0], [0,1,0],...]).
    radius : float, optional
        The radius of the tubes.
    segments : int, optional
        Number of segments for the tube's cross-section.
    end_caps : bool, optional
        If True, adds flat caps to the ends of each tube.
    flat_shading : bool, optional
        If True, use flat shading; otherwise, smooth shading is used.
    material : str, optional
        Material model (e.g., 'phong', 'basic').
    enable_picking : bool, optional
        If True, the actor can be picked in a 3D scene.

    Returns
    -------
    Actor
        A mesh actor containing the generated streamtubes.
    """

    def task(points):
        """Task to generate tube geometry for a single line.

        Parameters
        ----------
        points : ndarray, shape (N, 3)
            The 3D points defining the line.

        Returns
        -------
        tuple
            A tuple containing the vertices and indices for the tube geometry.
        """
        # Ensure points are float32 for consistency with Numba functions
        points_arr = np.asarray(points, dtype=np.float32)
        return generate_tube_geometry(points_arr, segments, radius, end_caps)

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(task, lines))

    all_vertices = []
    all_triangles = []
    vertex_offset = 0

    if not any(r[0].size > 0 for r in results):
        geo = buffer_to_geometry(
            indices=np.zeros((0, 3), dtype=np.int32),
            positions=np.zeros((0, 3), dtype=np.float32),
            colors=np.zeros((0, 4), dtype=np.float32),
        )
        mat = _create_mesh_material()
        obj = create_mesh(geometry=geo, material=mat)

    for verts, tris in results:
        if verts.size > 0 and tris.size > 0:
            all_vertices.append(verts)
            all_triangles.append(tris + vertex_offset)
            vertex_offset += verts.shape[0]

    final_vertices = np.vstack(all_vertices)
    final_triangles = np.vstack(all_triangles)

    n_vertices = final_vertices.shape[0]
    input_colors = np.asarray(colors)

    if input_colors.ndim == 1:
        vertex_colors = np.tile(input_colors, (n_vertices, 1))
    elif input_colors.ndim == 2 and input_colors.shape[0] == len(lines):
        color_dim = input_colors.shape[1]
        vertex_colors = np.zeros((n_vertices, color_dim), dtype=np.float32)
        current_v_idx = 0
        for i, (verts, _) in enumerate(results):
            num_verts = verts.shape[0]
            if num_verts > 0:
                vertex_colors[current_v_idx : current_v_idx + num_verts] = input_colors[
                    i
                ]
                current_v_idx += num_verts
    else:
        raise ValueError(
            "Colors must be a single tuple (e.g., (1,0,0)) or an array of shape "
            f"(n_lines, 3|4), but got shape {input_colors.shape} "
            f"for {len(lines)} lines."
        )

    geo = buffer_to_geometry(
        indices=final_triangles.astype("int32"),
        positions=final_vertices.astype("float32"),
        colors=vertex_colors.astype("float32"),
    )

    mat = _create_mesh_material(
        material=material,
        opacity=opacity,
        enable_picking=enable_picking,
        flat_shading=flat_shading,
    )
    obj = create_mesh(geometry=geo, material=mat)
    return obj
