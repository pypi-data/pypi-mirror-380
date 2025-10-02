"""UI core module that describe UI abstract class."""

import abc

import numpy as np

from fury.decorators import warn_on_args_to_kwargs
from fury.deprecator import deprecate_with_version
from fury.geometry import buffer_to_geometry, create_mesh
from fury.lib import (
    plane_geometry,
)
from fury.material import (
    _create_mesh_material,
)
from fury.primitive import prim_ring
from fury.ui import UIContext
from fury.ui.helpers import Anchor, get_anchor_to_multiplier


class UI(object, metaclass=abc.ABCMeta):
    """An umbrella class for all UI elements.

    While adding UI elements to the scene, we go over all the sub-elements
    that come with it and add those to the scene automatically.

    Attributes
    ----------
    position : (float, float)
        Absolute coordinates (x, y) of the lower-left corner of this
        UI component.
    center : (float, float)
        Absolute coordinates (x, y) of the center of this UI component.
    size : (int, int)
        Width and height in pixels of this UI component.
    on_left_mouse_button_pressed: function
        Callback function for when the left mouse button is pressed.
    on_left_mouse_button_released: function
        Callback function for when the left mouse button is released.
    on_left_mouse_button_clicked: function
        Callback function for when clicked using the left mouse button
        (i.e. pressed -> released).
    on_left_mouse_double_clicked: function
        Callback function for when left mouse button is double clicked
        (i.e pressed -> released -> pressed -> released).
    on_left_mouse_button_dragged: function
        Callback function for when dragging using the left mouse button.
    on_right_mouse_button_pressed: function
        Callback function for when the right mouse button is pressed.
    on_right_mouse_button_released: function
        Callback function for when the right mouse button is released.
    on_right_mouse_button_clicked: function
        Callback function for when clicking using the right mouse button
        (i.e. pressed -> released).
    on_right_mouse_double_clicked: function
        Callback function for when right mouse button is double clicked
        (i.e pressed -> released -> pressed -> released).
    on_right_mouse_button_dragged: function
        Callback function for when dragging using the right mouse button.
    on_middle_mouse_button_pressed: function
        Callback function for when the middle mouse button is pressed.
    on_middle_mouse_button_released: function
        Callback function for when the middle mouse button is released.
    on_middle_mouse_button_clicked: function
        Callback function for when clicking using the middle mouse button
        (i.e. pressed -> released).
    on_middle_mouse_double_clicked: function
        Callback function for when middle mouse button is double clicked
        (i.e pressed -> released -> pressed -> released).
    on_middle_mouse_button_dragged: function
        Callback function for when dragging using the middle mouse button.
    on_key_press: function
        Callback function for when a keyboard key is pressed.

    Parameters
    ----------
    position : (float, float)
        Absolute pixel coordinates `(x, y)` which, in combination with
        `x_anchor` and `y_anchor`, define the initial placement of this
        UI component.
    x_anchor : str, optional
        Define the horizontal anchor point for `position`. Can be "LEFT",
        "CENTER", or "RIGHT". Defaults to "LEFT".
    y_anchor : str, optional
        Define the vertical anchor point for `position`. Can be "BOTTOM",
        "CENTER", or "TOP". Defaults to "BOTTOM".
    """

    def __init__(self, *, position=(0, 0), x_anchor=Anchor.LEFT, y_anchor=Anchor.TOP):
        """Init scene.

        Parameters
        ----------
        position : (float, float)
            Absolute pixel coordinates `(x, y)` which, in combination with
            `x_anchor` and `y_anchor`, define the initial placement of this
            UI component.
        x_anchor : str, optional
            Define the horizontal anchor point for `position`. Can be "LEFT",
            "CENTER", or "RIGHT". Defaults to "LEFT".
        y_anchor : str, optional
            Define the vertical anchor point for `position`. Can be "BOTTOM",
            "CENTER", or "TOP". Defaults to "BOTTOM".
        """
        self.use_y_down = True
        self._position = np.array([0, 0])
        self._children = []
        self._anchors = [x_anchor, y_anchor]

        self._setup()  # Setup needed actors and sub UI components.
        self.set_position(position, x_anchor, y_anchor)

        self.left_button_state = "released"
        self.right_button_state = "released"
        self.middle_button_state = "released"

        self.on_left_mouse_button_pressed = lambda event: None
        self.on_left_mouse_button_dragged = lambda event: None
        self.on_left_mouse_button_released = lambda event: None
        self.on_left_mouse_button_clicked = lambda event: None
        self.on_left_mouse_double_clicked = lambda event: None
        self.on_right_mouse_button_pressed = lambda event: None
        self.on_right_mouse_button_released = lambda event: None
        self.on_right_mouse_button_clicked = lambda event: None
        self.on_right_mouse_double_clicked = lambda event: None
        self.on_right_mouse_button_dragged = lambda event: None
        self.on_middle_mouse_button_pressed = lambda event: None
        self.on_middle_mouse_button_released = lambda event: None
        self.on_middle_mouse_button_clicked = lambda event: None
        self.on_middle_mouse_double_clicked = lambda event: None
        self.on_middle_mouse_button_dragged = lambda event: None
        self.on_key_press = lambda event: None

    @abc.abstractmethod
    def _setup(self):
        """Set up this UI component.

        This is where you should create all your needed actors and sub UI
        components.
        """
        msg = "Subclasses of UI must implement `_setup(self)`."
        raise NotImplementedError(msg)

    @deprecate_with_version(
        message=(
            "The `add_to_scene` method is deprecated as a part of Fury v2. "
            "This method is no longer needed, as the addition of UI elements "
            "and their hierarchy into the scene is now automatically handled "
            "by `fury.window.Scene.add()`."
        ),
        since="2.0.0a1",
        until="2.1.0",
    )
    def add_to_scene(self, scene):
        """Allow UI objects to add their own props to the scene.

        Parameters
        ----------
        scene : scene
            The scene object to which the UI element's actors should be added.
        """
        scene.add(self)

    @deprecate_with_version(
        message=(
            "The `add_callback` method is deprecated as a part of Fury v2. "
            "This method is no longer needed, as event callbacks are now "
            "directly added to the actor itself using `handle_events()`."
        ),
        since="2.0.0a1",
        until="2.1.0",
    )
    def add_callback(self):
        """Add a callback to a specific event for this UI component."""
        pass

    @property
    @deprecate_with_version(
        message=(
            "The `position` property getter is deprecated as a part of Fury v2. "
            "Please use `get_position(x_anchor=Anchor.LEFT, "
            "y_anchor=Anchor.BOTTOM)` instead."
        ),
        since="2.0.0a1",
        until="2.1.0",
    )
    def position(self):
        """Get the position of this UI component.

        Returns
        -------
        (float, float)
            The `(x, y)` pixel coordinates of the UI component's lower-left corner.
        """
        return self.get_position(x_anchor=Anchor.LEFT, y_anchor=Anchor.BOTTOM)

    @position.setter
    @deprecate_with_version(
        message=(
            "The `position` property setter is deprecated as a part of Fury v2. "
            "Please use `set_position(coords=coords, x_anchor=Anchor.LEFT, "
            "y_anchor=Anchor.BOTTOM)` instead."
        ),
        since="2.0.0a1",
        until="2.1.0",
    )
    def position(self, coords):
        """Set the position of this UI component.

        Parameters
        ----------
        coords : (float, float)
            Absolute pixel coordinates `(x, y)` for the UI components lower-left corner.
        """
        self.set_position(coords=coords, x_anchor=Anchor.LEFT, y_anchor=Anchor.BOTTOM)

    @property
    @deprecate_with_version(
        message=(
            "The `center` property getter is deprecated as a part of Fury v2. "
            "Please use `get_position(x_anchor=Anchor.CENTER, "
            "y_anchor=Anchor.CENTER)` instead."
        ),
        since="2.0.0a1",
        until="2.1.0",
    )
    def center(self):
        """Get the center position of this UI component.

        Returns
        -------
        (float, float)
            The `(x, y)` pixel coordinates of the UI component's center.
        """
        return self.get_position(x_anchor=Anchor.CENTER, y_anchor=Anchor.CENTER)

    @center.setter
    @deprecate_with_version(
        message=(
            "The `center` property setter is deprecated as a part of Fury v2. "
            "Please use `set_position(coords=coords, x_anchor=Anchor.CENTER, "
            "y_anchor=Anchor.CENTER)` instead."
        ),
        since="2.0.0a1",
        until="2.1.0",
    )
    def center(self, coords):
        """Set the center of this UI component.

        Parameters
        ----------
        coords : (float, float)
            Absolute pixel coordinates `(x, y)` for the UI components lower-left corner.
        """
        self.set_position(coords=coords, x_anchor=Anchor.CENTER, y_anchor=Anchor.CENTER)

    @deprecate_with_version(
        message=(
            "The `_set_position` method is deprecated as a part of Fury v2. "
            "Its functionality is now handled by `_update_actors_position`."
        ),
        since="2.0.0a1",
        until="2.1.0",
    )
    def _set_position(self, coords):
        """Update the position of the internal actors.

        Parameters
        ----------
        coords : (float, float)
            Absolute pixel coordinates `(x, y)` for the UI components lower-left corner.
        """
        pass

    @abc.abstractmethod
    def _get_actors(self):
        """Get the actors composing this UI component."""
        msg = "Subclasses of UI must implement `_get_actors(self)`."
        raise NotImplementedError(msg)

    @property
    def actors(self):
        """Get actors composing this UI component.

        Returns
        -------
        list
            List of actors composing this UI component.
        """
        return self._get_actors()

    def perform_position_validation(self, x_anchor, y_anchor):
        """Perform validation checks for anchor string and the 'size' property.

        Parameters
        ----------
        x_anchor : str
            Horizontal anchor string to validate (e.g., "LEFT", "CENTER", "RIGHT").
        y_anchor : str
            Vertical anchor string to validate (e.g., "TOP", "CENTER", "BOTTOM").
        """
        if not hasattr(self, "size"):
            msg = "Subclasses of UI must implement property `size`."
            raise NotImplementedError(msg)

        if x_anchor not in [Anchor.LEFT, Anchor.CENTER, Anchor.RIGHT]:
            raise ValueError(
                f"x_anchor should be one of these {', '.join([Anchor.LEFT, Anchor.CENTER, Anchor.RIGHT])} but received {x_anchor}"  # noqa: E501
            )

        if y_anchor not in [Anchor.TOP, Anchor.CENTER, Anchor.BOTTOM]:
            raise ValueError(
                f"y_anchor should be one of these {', '.join([Anchor.TOP, Anchor.CENTER, Anchor.BOTTOM])} but received {y_anchor}"  # noqa: E501
            )

    def set_actor_position(self, actor, center_position):
        """Set the position of the PyGfx actor.

        Parameters
        ----------
        actor : Mesh
            The PyGfx mesh actor whose position needs to be set.
        center_position : tuple or ndarray
            A 2-element array `(x, y)` representing the desired center
            position of the actor.
        """
        canvas_size = UIContext.get_canvas_size()

        actor.local.x = center_position[0]
        actor.local.y = (
            canvas_size[1] - center_position[1]
            if self.use_y_down
            else center_position[1]
        )

    def _update_ui_mode(self, switch_to_old_ui):
        """Update the UI element's internal state when the UI system mode changes.

        Parameters
        ----------
        switch_to_old_ui : bool
            A flag indicating whether to use the V1 (legacy) UI mode.
        """

        def invert_y_anchor(y_anchor):
            """Invert the Y-axis anchor string.

            Parameters
            ----------
            y_anchor : Anchor
                The anchor to be inverted.

            Returns
            -------
            Anchor
                The inverted anchor.
            """
            if y_anchor in (Anchor.TOP, Anchor.BOTTOM):
                return Anchor.BOTTOM
            else:
                return Anchor.CENTER

        if switch_to_old_ui:
            current_position = self.get_position(
                self._anchors[0], invert_y_anchor(self._anchors[1])
            )
            self.use_y_down = not switch_to_old_ui
            self.set_position(current_position, self._anchors[0], self._anchors[1])

            for child in self._children:
                child._update_ui_mode(switch_to_old_ui=switch_to_old_ui)

    def set_position(self, coords, x_anchor=Anchor.LEFT, y_anchor=Anchor.TOP):
        """Position this UI component according to the specified anchor.

        Parameters
        ----------
        coords : (float, float)
            Absolute pixel coordinates (x, y). These coordinates
            are interpreted based on `x_anchor` and `y_anchor`.
        x_anchor : str, optional
            Define the horizontal anchor point for `coords`. Can be "LEFT",
            "CENTER", or "RIGHT". Defaults to "LEFT".
        y_anchor : str, optional
            Define the vertical anchor point for `coords`. Can be "TOP",
            "CENTER", or "BOTTOM". Defaults to "TOP".
        """
        self.perform_position_validation(x_anchor=x_anchor, y_anchor=y_anchor)

        self._position = np.array(coords)
        self._anchors = [x_anchor.upper(), y_anchor.upper()]
        self._update_actors_position()

    def get_position(
        self,
        x_anchor=Anchor.LEFT,
        y_anchor=Anchor.TOP,
    ):
        """Get the position of this UI component according to the specified anchor.

        Parameters
        ----------
        x_anchor : str, optional
            Define the horizontal anchor point for the returned coordinates.
            Can be "LEFT", "CENTER", or "RIGHT". Defaults to "LEFT".
        y_anchor : str, optional
            Define the vertical anchor point for the returned coordinates.
            Can be "BOTTOM", "CENTER", or "TOP". Defaults to "TOP".

        Returns
        -------
        (float, float)
            The (x, y) pixel coordinates of the specified anchor point.
        """

        ANCHOR_TO_MULTIPLIER = get_anchor_to_multiplier(use_y_down=self.use_y_down)

        self.perform_position_validation(x_anchor=x_anchor, y_anchor=y_anchor)

        return np.array(
            [
                self._position[0]
                + self.size[0]
                * (
                    ANCHOR_TO_MULTIPLIER[x_anchor.upper()]
                    - ANCHOR_TO_MULTIPLIER[self._anchors[0].upper()]
                ),
                self._position[1]
                + self.size[1]
                * (
                    ANCHOR_TO_MULTIPLIER[y_anchor.upper()]
                    - ANCHOR_TO_MULTIPLIER[self._anchors[1].upper()]
                ),
            ]
        )

    @abc.abstractmethod
    def _update_actors_position(self):
        """Update the position of the internal actors."""
        msg = "Subclasses of UI must implement `_set_actors_position(self)`."
        raise NotImplementedError(msg)

    @property
    def size(self):
        """Get width and height of this UI component.

        Returns
        -------
        (int, int)
            Width and Height of UI component in pixels.
        """
        return np.asarray(self._get_size(), dtype=int)

    @abc.abstractmethod
    def _get_size(self):
        """Get the actual size of the UI component.

        Returns
        -------
        (int, int)
            Width and height of the UI component in pixels.
        """
        msg = "Subclasses of UI must implement property `size`."
        raise NotImplementedError(msg)

    def set_visibility(self, visibility):
        """Set visibility of this UI component.

        Parameters
        ----------
        visibility : bool
            If `True`, the UI component will be visible. If `False`, it will be hidden.
        """
        for actor in self.actors:
            # actor.SetVisibility(visibility)
            actor.visible = visibility

    def handle_events(self, actor):
        """Attach event handlers to the UI object.

        Parameters
        ----------
        actor : Mesh
            The PyGfx mesh to which event handlers should be attached.
        """
        actor.add_event_handler(self.mouse_button_down_callback, "pointer_down")
        actor.add_event_handler(self.mouse_button_up_callback, "pointer_up")
        actor.add_event_handler(self.mouse_move_callback, "pointer_move")
        actor.add_event_handler(self.key_press_callback, "key_up")

    def mouse_button_down_callback(self, event):
        """Handle mouse button press event.

        Parameters
        ----------
        event : PointerEvent
            The PyGfx pointer event object.
        """
        if event.button == 1:
            self.left_button_click_callback(event)
        elif event.button == 2:
            self.right_button_click_callback(event)
        elif event.button == 3:
            self.middle_button_click_callback(event)
        event.cancel()

    def mouse_button_up_callback(self, event):
        """Handle mouse button release event.

        Parameters
        ----------
        event : PointerEvent
            The PyGfx pointer event object.
        """
        if event.button == 1:
            self.left_button_release_callback(event)
        elif event.button == 2:
            self.right_button_release_callback(event)
        elif event.button == 3:
            self.middle_button_release_callback(event)
        event.cancel()

    def left_button_click_callback(self, event):
        """Handle left mouse button press event.

        Parameters
        ----------
        event : PointerEvent
            The PyGfx pointer event object.
        """
        self.left_button_state = "pressing"
        self.on_left_mouse_button_pressed(event)

    def left_button_release_callback(self, event):
        """Handle left mouse button release event.

        Parameters
        ----------
        event : PointerEvent
            The PyGfx pointer event object.
        """
        if self.left_button_state == "pressing":
            self.on_left_mouse_button_clicked(event)
        self.left_button_state = "released"
        self.on_left_mouse_button_released(event)

    def right_button_click_callback(self, event):
        """Handle right mouse button press event.

        Parameters
        ----------
        event : PointerEvent
            The PyGfx pointer event object.
        """
        self.right_button_state = "pressing"
        self.on_right_mouse_button_pressed(event)

    def right_button_release_callback(self, event):
        """Handle right mouse button release event.

        Parameters
        ----------
        event : PointerEvent
            The PyGfx pointer event object.
        """
        if self.right_button_state == "pressing":
            self.on_right_mouse_button_clicked(event)
        self.right_button_state = "released"
        self.on_right_mouse_button_released(event)

    def middle_button_click_callback(self, event):
        """Handle middle mouse button press event.

        Parameters
        ----------
        event : PointerEvent
            The PyGfx pointer event object.
        """
        self.middle_button_state = "pressing"
        self.on_middle_mouse_button_pressed(event)

    def middle_button_release_callback(self, event):
        """Handle middle mouse button release event.

        Parameters
        ----------
        event : PointerEvent
            The PyGfx pointer event object.
        """
        if self.middle_button_state == "pressing":
            self.on_middle_mouse_button_clicked(event)
        self.middle_button_state = "released"
        self.on_middle_mouse_button_released(event)

    def mouse_move_callback(self, event):
        """Handle mouse move event.

        Parameters
        ----------
        event : PointerEvent
            The PyGfx pointer event object.
        """
        left_pressing_or_dragging = (
            self.left_button_state == "pressing" or self.left_button_state == "dragging"
        )

        right_pressing_or_dragging = (
            self.right_button_state == "pressing"
            or self.right_button_state == "dragging"
        )

        middle_pressing_or_dragging = (
            self.middle_button_state == "pressing"
            or self.middle_button_state == "dragging"
        )

        if left_pressing_or_dragging:
            self.left_button_state = "dragging"
            self.on_left_mouse_button_dragged(event)
        elif right_pressing_or_dragging:
            self.right_button_state = "dragging"
            self.on_right_mouse_button_dragged(event)
        elif middle_pressing_or_dragging:
            self.middle_button_state = "dragging"
            self.on_middle_mouse_button_dragged(event)

    def key_press_callback(self, event):
        """Handle key press event.

        Parameters
        ----------
        event : KeyboardEvent
            The PyGfx keyboard event object.
        """
        self.on_key_press(event)


class Rectangle2D(UI):
    """A 2D rectangle sub-classed from UI.

    Parameters
    ----------
    size : (int, int), optional
        Initial `(width, height)` of the rectangle in pixels.
        Defaults to `(0, 0)`.
    position : (float, float), optional
        Coordinates `(x, y)` of the rectangle. The interpretation of `(x,y)`
        (e.g., top-left, bottom-left) depends on the current UI version.
        Defaults to `(0, 0)`.
    color : (float, float, float), optional
        RGB color tuple, with values in the range `[0, 1]`.
        Defaults to `(1, 1, 1)` (white).
    opacity : float, optional
        Degree of transparency, with values in the range `[0, 1]`.
        `0` is fully transparent, `1` is fully opaque. Defaults to `1.0`.
    """

    @warn_on_args_to_kwargs()
    def __init__(self, *, size=(0, 0), position=(0, 0), color=(1, 1, 1), opacity=1.0):
        """Initialize a rectangle.

        Parameters
        ----------
        size : (int, int)
            The size of the rectangle (width, height) in pixels.
        position : (float, float)
            Coordinates (x, y) of the lower-left corner of the rectangle.
        color : (float, float, float)
            Must take values in [0, 1].
        opacity : float
            Must take values in [0, 1].
        """
        super(Rectangle2D, self).__init__(position=position)
        self.color = color
        self.opacity = opacity
        self.resize(size)

    def _setup(self):
        """Set up this UI component.

        Create the plane actor used internally.
        """
        geo = plane_geometry(width=1, height=1)
        mat = _create_mesh_material(
            material="basic", enable_picking=True, flat_shading=True
        )
        self.actor = create_mesh(geometry=geo, material=mat)

        self.handle_events(self.actor)

    def _get_actors(self):
        """Get the actors composing this UI component.

        Returns
        -------
        list
            List of actors composing this UI component.
        """
        return [self.actor]

    def _get_size(self):
        """Get the current size of the rectangle actor.

        Returns
        -------
        (float, float)
            The current `(width, height)` of the rectangle in pixels.
        """
        bounds = self.actor.get_bounding_box()
        minx, miny, minz = bounds[0]
        maxx, maxy, maxz = bounds[1]
        return [maxx - minx, maxy - miny]

    @property
    def width(self):
        """Get the current width of the rectangle.

        Returns
        -------
        float
            The width of the rectangle in pixels.
        """
        return self._get_size()[0]

    @width.setter
    def width(self, width):
        """Set the width of the rectangle.

        Parameters
        ----------
        width : float
            New width of the rectangle.
        """
        self.resize((width, self.height))

    @property
    def height(self):
        """Get the current height of the rectangle.

        Returns
        -------
        float
            The height of the rectangle in pixels.
        """
        return self._get_size()[1]

    @height.setter
    def height(self, height):
        """Set the height of the rectangle.

        Parameters
        ----------
        height : float
            New height of the rectangle.
        """
        self.resize((self.width, height))

    def resize(self, size):
        """Set the rectangle size.

        Parameters
        ----------
        size : (float, float)
            Rectangle size (width, height) in pixels.
        """
        self.actor.geometry = plane_geometry(width=size[0], height=size[1])
        self._update_actors_position()

    def _update_actors_position(self):
        """Set the position of the internal actor."""
        position = self.get_position(x_anchor=Anchor.CENTER, y_anchor=Anchor.CENTER)

        self.set_actor_position(self.actor, position)

    @property
    def color(self):
        """Get the rectangle color.

        Returns
        -------
        (float, float, float)
            RGB color.
        """
        return self.actor.material.color

    @color.setter
    def color(self, color):
        """Set the rectangle color.

        Parameters
        ----------
        color : (float, float, float)
            RGB. Must take values in [0, 1].
        """
        self.actor.material.color = np.array([*color, 1.0])

    @property
    def opacity(self):
        """Get the rectangle opacity.

        Returns
        -------
        float
            Opacity value.
        """
        return self.actor.material.opacity

    @opacity.setter
    def opacity(self, opacity):
        """Set the rectangle opacity.

        Parameters
        ----------
        opacity : float
            Degree of transparency. Must be between [0, 1].
        """
        self.actor.material.opacity = opacity


class Disk2D(UI):
    """A 2D disk UI component.

    Parameters
    ----------
    outer_radius : int
        Outer radius of the disk.
    inner_radius : int
        Inner radius of the disk.
    center : (float, float), optional
        Coordinates (x, y) of the center of the disk.
    color : (float, float, float), optional
        Must take values in [0, 1].
    opacity : float, optional
        Must take values in [0, 1].
    """

    @warn_on_args_to_kwargs()
    def __init__(
        self,
        outer_radius,
        *,
        inner_radius=0,
        center=(0, 0),
        color=(1, 1, 1),
        opacity=1.0,
    ):
        """Initialize a 2D Disk.

        Parameters
        ----------
        outer_radius : int
            Outer radius of the disk.
        inner_radius : int, optional
            Inner radius of the disk.
        center : (float, float), optional
            Coordinates (x, y) of the center of the disk.
        color : (float, float, float), optional
            Must take values in [0, 1].
        opacity : float, optional
            Must take values in [0, 1].
        """
        self.actor = None
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius

        super(Disk2D, self).__init__(
            position=center, x_anchor=Anchor.CENTER, y_anchor=Anchor.CENTER
        )

        self.color = color
        self.opacity = opacity

    def _setup(self):
        """Set up this UI component.

        Create the disk actor used internally.
        """
        positions, indices = prim_ring(
            inner_radius=self.inner_radius, outer_radius=self.outer_radius
        )
        geo = buffer_to_geometry(positions=positions, indices=indices)
        mat = _create_mesh_material(
            material="basic", enable_picking=True, flat_shading=True
        )
        self.actor = create_mesh(geometry=geo, material=mat)

        self.handle_events(self.actor)

    def _get_actors(self):
        """Get the actors composing this UI component.

        Returns
        -------
        list
            List of actors composing this UI component.
        """
        return [self.actor]

    def _get_size(self):
        """Get the current size of the disk.

        Returns
        -------
        (float, float)
            The current `(diameter, diameter)` of the disk in pixels.
        """
        diameter = 2 * self.outer_radius
        size = (diameter, diameter)
        return size

    def _update_actors_position(self):
        """Set the position of the internal actor."""
        position = self.get_position(x_anchor=Anchor.CENTER, y_anchor=Anchor.CENTER)

        self.set_actor_position(self.actor, position)

    @property
    def color(self):
        """Get the color of this UI component.

        Returns
        -------
        (float, float, float)
            RGB color.
        """
        return self.actor.material.color

    @color.setter
    def color(self, color):
        """Set the color of this UI component.

        Parameters
        ----------
        color : (float, float, float)
            RGB. Must take values in [0, 1].
        """
        self.actor.material.color = np.array([*color, 1.0])

    @property
    def opacity(self):
        """Get the opacity of this UI component.

        Returns
        -------
        float
            Opacity value.
        """
        return self.actor.material.opacity

    @opacity.setter
    def opacity(self, opacity):
        """Set the opacity of this UI component.

        Parameters
        ----------
        opacity : float
            Degree of transparency. Must be between [0, 1].
        """
        self.actor.material.opacity = opacity

    @property
    def outer_radius(self):
        """Get the outer radius of the disk.

        Returns
        -------
        int
            Outer radius in pixels.
        """
        return self._outer_radius

    @outer_radius.setter
    def outer_radius(self, radius):
        """Set the outer radius of the disk.

        Parameters
        ----------
        radius : int
            New outer radius.
        """
        if self.actor:
            positions, indices = prim_ring(
                inner_radius=self.inner_radius, outer_radius=radius
            )
            self.actor.geometry = buffer_to_geometry(
                positions=positions, indices=indices
            )
        self._outer_radius = radius

    @property
    def inner_radius(self):
        """Get the inner radius of the disk.

        Returns
        -------
        int
            Inner radius in pixels.
        """
        return self._inner_radius

    @inner_radius.setter
    def inner_radius(self, radius):
        """Set the inner radius of the disk.

        Parameters
        ----------
        radius : int
            New inner radius.
        """
        if self.actor:
            positions, indices = prim_ring(
                inner_radius=radius, outer_radius=self.outer_radius
            )
            self.actor.geometry = buffer_to_geometry(
                positions=positions, indices=indices
            )
        self._inner_radius = radius


# class TextBlock2D(UI):
#     """Wrap over the default vtkTextActor and helps setting the text.

#     Contains member functions for text formatting.

#     Attributes
#     ----------
#     actor : :class:`vtkTextActor`
#         The text actor.
#     message : str
#         The initial text while building the actor.
#     position : (float, float)
#         (x, y) in pixels.
#     color : (float, float, float)
#         RGB: Values must be between 0-1.
#     bg_color : (float, float, float)
#         RGB: Values must be between 0-1.
#     font_size : int
#         Size of the text font.
#     font_family : str
#         Currently only supports Arial.
#     justification : str
#         left, right or center.
#     vertical_justification : str
#         bottom, middle or top.
#     bold : bool
#         Makes text bold.
#     italic : bool
#         Makes text italicised.
#     shadow : bool
#         Adds text shadow.
#     size : (int, int)
#         Size (width, height) in pixels of the text bounding box.
#     auto_font_scale : bool
#         Automatically scale font according to the text bounding box.
#     dynamic_bbox : bool
#         Automatically resize the bounding box according to the content.

#     """

#     @warn_on_args_to_kwargs()
#     def __init__(
#         self,
#         *,
#         text="Text Block",
#         font_size=18,
#         font_family="Arial",
#         justification="left",
#         vertical_justification="bottom",
#         bold=False,
#         italic=False,
#         shadow=False,
#         size=None,
#         color=(1, 1, 1),
#         bg_color=None,
#         position=(0, 0),
#         auto_font_scale=False,
#         dynamic_bbox=False,
#     ):
#         """Init class instance.

#         Parameters
#         ----------
#         text : str
#             The initial text while building the actor.
#         position : (float, float)
#             (x, y) in pixels.
#         color : (float, float, float)
#             RGB: Values must be between 0-1.
#         bg_color : (float, float, float)
#             RGB: Values must be between 0-1.
#         font_size : int
#             Size of the text font.
#         font_family : str
#             Currently only supports Arial.
#         justification : str
#             left, right or center.
#         vertical_justification : str
#             bottom, middle or top.
#         bold : bool
#             Makes text bold.
#         italic : bool
#             Makes text italicised.
#         shadow : bool
#             Adds text shadow.
#         size : (int, int)
#             Size (width, height) in pixels of the text bounding box.
#         auto_font_scale : bool, optional
#             Automatically scale font according to the text bounding box.
#         dynamic_bbox : bool, optional
#             Automatically resize the bounding box according to the content.

#         """
#         self.boundingbox = [0, 0, 0, 0]
#         super(TextBlock2D, self).__init__(position=position)
#         self.scene = None
#         self.have_bg = bool(bg_color)
#         self.color = color
#         self.background_color = bg_color
#         self.font_family = font_family
#         self._justification = justification
#         self.bold = bold
#         self.italic = italic
#         self.shadow = shadow
#         self._vertical_justification = vertical_justification
#         self._dynamic_bbox = dynamic_bbox
#         self.auto_font_scale = auto_font_scale
#         self.message = text
#         self.font_size = font_size
#         if size is not None:
#             self.resize(size)
#         elif not self.dynamic_bbox:
#             # raise ValueError("TextBlock size is required as it is not dynamic.")
#             self.resize((0, 0))

#     def _setup(self):
#         self.actor = TextActor()
#         self.actor.GetPosition2Coordinate().SetCoordinateSystemToViewport()
#         self.background = Rectangle2D()
#         self.handle_events(self.actor)

#     def resize(self, size):
#         """Resize TextBlock2D.

#         Parameters
#         ----------
#         size : (int, int)
#             Text bounding box size(width, height) in pixels.

#         """
#         self.update_bounding_box(size=size)

#     def _get_actors(self):
#         """Get the actors composing this UI component."""
#         return [self.actor] + self.background.actors

#     def _add_to_scene(self, scene):
#         """Add all subcomponents or VTK props that compose this UI component.

#         Parameters
#         ----------
#         scene : scene

#         """
#         scene.add(self.background, self.actor)

#     @property
#     def message(self):
#         """Get message from the text.

#         Returns
#         -------
#         str
#             The current text message.

#         """
#         return self.actor.GetInput()

#     @message.setter
#     def message(self, text):
#         """Set the text message.

#         Parameters
#         ----------
#         text : str
#             The message to be set.

#         """
#         self.actor.SetInput(text)
#         if self.dynamic_bbox:
#             self.update_bounding_box()

#     @property
#     def font_size(self):
#         """Get text font size.

#         Returns
#         -------
#         int
#             Text font size.

#         """
#         return self.actor.GetTextProperty().GetFontSize()

#     @font_size.setter
#     def font_size(self, size):
#         """Set font size.

#         Parameters
#         ----------
#         size : int
#             Text font size.

#         """
#         if not self.auto_font_scale:
#             self.actor.SetTextScaleModeToNone()
#             self.actor.GetTextProperty().SetFontSize(size)

#         if self.dynamic_bbox:
#             self.update_bounding_box()

#     @property
#     def font_family(self):
#         """Get font family.

#         Returns
#         -------
#         str
#             Text font family.

#         """
#         return self.actor.GetTextProperty().GetFontFamilyAsString()

#     @font_family.setter
#     def font_family(self, family="Arial"):
#         """Set font family.

#         Currently Arial and Courier are supported.

#         Parameters
#         ----------
#         family : str
#             The font family.

#         """
#         if family == "Arial":
#             self.actor.GetTextProperty().SetFontFamilyToArial()
#         elif family == "Courier":
#             self.actor.GetTextProperty().SetFontFamilyToCourier()
#         else:
#             raise ValueError("Font not supported yet: {}.".format(family))

#     @property
#     def justification(self):
#         """Get text justification.

#         Returns
#         -------
#         str
#             Text justification.

#         """
#         return self._justification

#     @justification.setter
#     def justification(self, justification):
#         """Justify text.

#         Parameters
#         ----------
#         justification : str
#             Possible values are left, right, center.

#         """
#         self._justification = justification
#         self.update_alignment()

#     @property
#     def vertical_justification(self):
#         """Get text vertical justification.

#         Returns
#         -------
#         str
#             Text vertical justification.

#         """
#         return self._vertical_justification

#     @vertical_justification.setter
#     def vertical_justification(self, vertical_justification):
#         """Justify text vertically.

#         Parameters
#         ----------
#         vertical_justification : str
#             Possible values are bottom, middle, top.

#         """
#         self._vertical_justification = vertical_justification
#         self.update_alignment()

#     @property
#     def bold(self):
#         """Return whether the text is bold.

#         Returns
#         -------
#         bool
#             Text is bold if True.

#         """
#         return self.actor.GetTextProperty().GetBold()

#     @bold.setter
#     def bold(self, flag):
#         """Bold/un-bold text.

#         Parameters
#         ----------
#         flag : bool
#             Sets text bold if True.

#         """
#         self.actor.GetTextProperty().SetBold(flag)

#     @property
#     def italic(self):
#         """Return whether the text is italicised.

#         Returns
#         -------
#         bool
#             Text is italicised if True.

#         """
#         return self.actor.GetTextProperty().GetItalic()

#     @italic.setter
#     def italic(self, flag):
#         """Italicise/un-italicise text.

#         Parameters
#         ----------
#         flag : bool
#             Italicises text if True.

#         """
#         self.actor.GetTextProperty().SetItalic(flag)

#     @property
#     def shadow(self):
#         """Return whether the text has shadow.

#         Returns
#         -------
#         bool
#             Text is shadowed if True.

#         """
#         return self.actor.GetTextProperty().GetShadow()

#     @shadow.setter
#     def shadow(self, flag):
#         """Add/remove text shadow.

#         Parameters
#         ----------
#         flag : bool
#             Shadows text if True.

#         """
#         self.actor.GetTextProperty().SetShadow(flag)

#     @property
#     def color(self):
#         """Get text color.

#         Returns
#         -------
#         (float, float, float)
#             Returns text color in RGB.

#         """
#         return self.actor.GetTextProperty().GetColor()

#     @color.setter
#     def color(self, color=(1, 0, 0)):
#         """Set text color.

#         Parameters
#         ----------
#         color : (float, float, float)
#             RGB: Values must be between 0-1.

#         """
#         self.actor.GetTextProperty().SetColor(*color)

#     @property
#     def background_color(self):
#         """Get background color.

#         Returns
#         -------
#         (float, float, float) or None
#             If None, there no background color.
#             Otherwise, background color in RGB.

#         """
#         if not self.have_bg:
#             return None

#         return self.background.color

#     @background_color.setter
#     def background_color(self, color):
#         """Set text color.

#         Parameters
#         ----------
#         color : (float, float, float) or None
#             If None, remove background.
#             Otherwise, RGB values (must be between 0-1).

#         """
#         if color is None:
#             # Remove background.
#             self.have_bg = False
#             self.background.set_visibility(False)

#         else:
#             self.have_bg = True
#             self.background.set_visibility(True)
#             self.background.color = color

#     @property
#     def auto_font_scale(self):
#         """Return whether text font is automatically scaled.

#         Returns
#         -------
#         bool
#             Text is auto_font_scaled if True.

#         """
#         return self._auto_font_scale

#     @auto_font_scale.setter
#     def auto_font_scale(self, flag):
#         """Add/remove text auto_font_scale.

#         Parameters
#         ----------
#         flag : bool
#             Automatically scales the text font if True.

#         """
#         self._auto_font_scale = flag
#         if flag:
#             self.actor.SetTextScaleModeToProp()
#             self._justification = "left"
#             self.update_bounding_box(size=self.size)
#         else:
#             self.actor.SetTextScaleModeToNone()

#     @property
#     def dynamic_bbox(self):
#         """Automatically resize the bounding box according to the content.

#         Returns
#         -------
#         bool
#             Bounding box is dynamic if True.

#         """
#         return self._dynamic_bbox

#     @dynamic_bbox.setter
#     def dynamic_bbox(self, flag):
#         """Add/remove dynamic_bbox.

#         Parameters
#         ----------
#         flag : bool
#             The text bounding box is dynamic if True.

#         """
#         self._dynamic_bbox = flag
#         if flag:
#             self.update_bounding_box()

#     def update_alignment(self):
#         """Update Text Alignment."""
#         text_property = self.actor.GetTextProperty()
#         updated_text_position = [0, 0]

#         if self.justification.lower() == "left":
#             text_property.SetJustificationToLeft()
#             updated_text_position[0] = self.boundingbox[0]
#         elif self.justification.lower() == "center":
#             text_property.SetJustificationToCentered()
#             updated_text_position[0] = (
#                 self.boundingbox[0] + (self.boundingbox[2] - self.boundingbox[0]) // 2
#             )
#         elif self.justification.lower() == "right":
#             text_property.SetJustificationToRight()
#             updated_text_position[0] = self.boundingbox[2]
#         else:
#             msg = "Text can only be justified left, right and center."
#             raise ValueError(msg)

#         if self.vertical_justification.lower() == "bottom":
#             text_property.SetVerticalJustificationToBottom()
#             updated_text_position[1] = self.boundingbox[1]
#         elif self.vertical_justification.lower() == "middle":
#             text_property.SetVerticalJustificationToCentered()
#             updated_text_position[1] = (
#                 self.boundingbox[1] + (self.boundingbox[3] - self.boundingbox[1]) // 2
#             )
#         elif self.vertical_justification.lower() == "top":
#             text_property.SetVerticalJustificationToTop()
#             updated_text_position[1] = self.boundingbox[3]
#         else:
#             msg = "Vertical justification must be: bottom, middle or top."
#             raise ValueError(msg)

#         self.actor.SetPosition(updated_text_position)

#     def cal_size_from_message(self):
#         """Calculate size of background according to the message it contains."""
#         lines = self.message.split("\n")
#         max_length = max(len(line) for line in lines)
#         return [max_length * self.font_size, len(lines) * self.font_size]

#     @warn_on_args_to_kwargs()
#     def update_bounding_box(self, *, size=None):
#         """Update Text Bounding Box.

#         Parameters
#         ----------
#         size : (int, int) or None
#             If None, calculates bounding box.
#             Otherwise, uses the given size.

#         """
#         if size is None:
#             size = self.cal_size_from_message()

#         self.boundingbox = [
#             self.position[0],
#             self.position[1],
#             self.position[0] + size[0],
#             self.position[1] + size[1],
#         ]
#         self.background.resize(size)

#         if self.auto_font_scale:
#             self.actor.SetPosition2(
#                 self.boundingbox[2] - self.boundingbox[0],
#                 self.boundingbox[3] - self.boundingbox[1],
#             )
#         else:
#             self.update_alignment()

#     def _set_position(self, position):
#         """Set text actor position.

#         Parameters
#         ----------
#         position : (float, float)
#             The new position. (x, y) in pixels.

#         """
#         self.actor.SetPosition(*position)
#         self.background.position = position

#     def _get_size(self):
#         bb_size = (
#             self.boundingbox[2] - self.boundingbox[0],
#             self.boundingbox[3] - self.boundingbox[1],
#         )
#         if self.dynamic_bbox or self.auto_font_scale or sum(bb_size):
#             return bb_size
#         return self.cal_size_from_message()


# class Button2D(UI):
#     """A 2D overlay button and is of type vtkTexturedActor2D.

#     Currently supports::

#         - Multiple icons.
#         - Switching between icons.

#     """

#     @warn_on_args_to_kwargs()
#     def __init__(self, icon_fnames, *, position=(0, 0), size=(30, 30)):
#         """Init class instance.

#         Parameters
#         ----------
#         icon_fnames : List(string, string)
#             ((iconname, filename), (iconname, filename), ....)
#         position : (float, float), optional
#             Absolute coordinates (x, y) of the lower-left corner of the button.
#         size : (int, int), optional
#             Width and height in pixels of the button.

#         """
#         super(Button2D, self).__init__(position=position)

#         self.icon_extents = {}
#         self.icons = self._build_icons(icon_fnames)
#         self.icon_names = [icon[0] for icon in self.icons]
#         self.current_icon_id = 0
#         self.current_icon_name = self.icon_names[self.current_icon_id]
#         self.set_icon(self.icons[self.current_icon_id][1])
#         self.resize(size)

#     def _get_size(self):
#         lower_left_corner = self.texture_points.GetPoint(0)
#         upper_right_corner = self.texture_points.GetPoint(2)
#         size = np.array(upper_right_corner) - np.array(lower_left_corner)
#         return abs(size[:2])

#     def _build_icons(self, icon_fnames):
#         """Convert file names to ImageData.

#         A pre-processing step to prevent re-read of file names during every
#         state change.

#         Parameters
#         ----------
#         icon_fnames : List(string, string)
#             ((iconname, filename), (iconname, filename), ....)

#         Returns
#         -------
#         icons : List
#             A list of corresponding ImageData.

#         """
#         icons = []
#         for icon_name, icon_fname in icon_fnames:
#             icons.append((icon_name, load_image(icon_fname, as_vtktype=True)))

#         return icons

#     def _setup(self):
#         """Set up this UI component.

#         Creating the button actor used internally.

#         """
#         # This is highly inspired by
#         # https://github.com/Kitware/VTK/blob/c3ec2495b183e3327820e927af7f8f90d34c3474/Interaction/Widgets/vtkBalloonRepresentation.cxx#L47

#         self.texture_polydata = PolyData()
#         self.texture_points = Points()
#         self.texture_points.SetNumberOfPoints(4)

#         polys = CellArray()
#         polys.InsertNextCell(4)
#         polys.InsertCellPoint(0)
#         polys.InsertCellPoint(1)
#         polys.InsertCellPoint(2)
#         polys.InsertCellPoint(3)
#         self.texture_polydata.SetPolys(polys)

#         tc = FloatArray()
#         tc.SetNumberOfComponents(2)
#         tc.SetNumberOfTuples(4)
#         tc.InsertComponent(0, 0, 0.0)
#         tc.InsertComponent(0, 1, 0.0)
#         tc.InsertComponent(1, 0, 1.0)
#         tc.InsertComponent(1, 1, 0.0)
#         tc.InsertComponent(2, 0, 1.0)
#         tc.InsertComponent(2, 1, 1.0)
#         tc.InsertComponent(3, 0, 0.0)
#         tc.InsertComponent(3, 1, 1.0)
#         self.texture_polydata.GetPointData().SetTCoords(tc)

#         texture_mapper = PolyDataMapper2D()
#         texture_mapper = set_input(texture_mapper, self.texture_polydata)

#         button = TexturedActor2D()
#         button.SetMapper(texture_mapper)

#         self.texture = Texture()
#         button.SetTexture(self.texture)

#         button_property = Property2D()
#         button_property.SetOpacity(1.0)
#         button.SetProperty(button_property)
#         self.actor = button

#         # Add default events listener to the VTK actor.
#         self.handle_events(self.actor)

#     def _get_actors(self):
#         """Get the actors composing this UI component."""
#         return [self.actor]

#     def _add_to_scene(self, scene):
#         """Add all subcomponents or VTK props that compose this UI component.

#         Parameters
#         ----------
#         scene : scene

#         """
#         scene.add(self.actor)

#     def resize(self, size):
#         """Resize the button.

#         Parameters
#         ----------
#         size : (float, float)
#             Button size (width, height) in pixels.

#         """
#         # Update actor.
#         self.texture_points.SetPoint(0, 0, 0, 0.0)
#         self.texture_points.SetPoint(1, size[0], 0, 0.0)
#         self.texture_points.SetPoint(2, size[0], size[1], 0.0)
#         self.texture_points.SetPoint(3, 0, size[1], 0.0)
#         self.texture_polydata.SetPoints(self.texture_points)

#     def _set_position(self, coords):
#         """Set the lower-left corner position of this UI component.

#         Parameters
#         ----------
#         coords: (float, float)
#             Absolute pixel coordinates (x, y).

#         """
#         self.actor.SetPosition(*coords)

#     @property
#     def color(self):
#         """Get the button's color."""
#         color = self.actor.GetProperty().GetColor()
#         return np.asarray(color)

#     @color.setter
#     def color(self, color):
#         """Set the button's color.

#         Parameters
#         ----------
#         color : (float, float, float)
#             RGB. Must take values in [0, 1].

#         """
#         self.actor.GetProperty().SetColor(*color)

#     def scale(self, factor):
#         """Scale the button.

#         Parameters
#         ----------
#         factor : (float, float)
#             Scaling factor (width, height) in pixels.

#         """
#         self.resize(self.size * factor)

#     def set_icon_by_name(self, icon_name):
#         """Set the button icon using its name.

#         Parameters
#         ----------
#         icon_name : str

#         """
#         icon_id = self.icon_names.index(icon_name)
#         self.set_icon(self.icons[icon_id][1])

#     def set_icon(self, icon):
#         """Modify the icon used by the vtkTexturedActor2D.

#         Parameters
#         ----------
#         icon : imageData

#         """
#         self.texture = set_input(self.texture, icon)

#     def next_icon_id(self):
#         """Set the next icon ID while cycling through icons."""
#         self.current_icon_id += 1
#         if self.current_icon_id == len(self.icons):
#             self.current_icon_id = 0
#         self.current_icon_name = self.icon_names[self.current_icon_id]

#     def next_icon(self):
#         """Increment the state of the Button.

#         Also changes the icon.
#         """
#         self.next_icon_id()
#         self.set_icon(self.icons[self.current_icon_id][1])
