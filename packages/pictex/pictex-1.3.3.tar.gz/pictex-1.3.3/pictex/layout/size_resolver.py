from __future__ import annotations
from typing import TYPE_CHECKING
import skia

if TYPE_CHECKING:
    from ..nodes import Node
    from ..models import SizeValue

class SizeResolver:

    def __init__(self, node: Node):
        self._node = node
        self._intrinsic_bounds: skia.Rect | None = None
    
    def resolve_width(self) -> int:
        forced_width = self._node.forced_size[0]
        if forced_width is not None:
            spacing = self._get_horizontal_spacing()
            return max(0, forced_width - spacing)

        return self._resolve_width_from_style()

    def resolve_height(self) -> int:
        forced_height = self._node.forced_size[1]
        if forced_height is not None:
            spacing = self._get_vertical_spacing()
            return max(0, forced_height - spacing)

        return self._resolve_height_from_style()
    
    def _get_horizontal_spacing(self) -> float:
        padding = self._node.computed_styles.padding.get()
        border = self._node.computed_styles.border.get()
        border_width = border.width if border else 0
        return padding.left + padding.right + (border_width * 2)
    
    def _get_vertical_spacing(self) -> float:
        padding = self._node.computed_styles.padding.get()
        border = self._node.computed_styles.border.get()
        border_width = border.width if border else 0
        return padding.top + padding.bottom + (border_width * 2)

    def _get_axis_size(self, value: 'SizeValue', axis: str, outer_space: float) -> float:
        if value.mode == 'absolute':
            return value.value - outer_space
        if value.mode == 'percent':
            return self._get_parent_percent_axis_size(axis, value.value / 100.0) - outer_space
        if value.mode == 'fit-content' or value.mode == 'auto':
            return self._get_intrinsic_axis_size(axis)
        if value.mode == 'fill-available':
            return self._get_parent_available_axis_size_per_child(axis)
        if value.mode == 'fit-background-image':
            return self._get_background_image_axis_size(axis) - outer_space
        raise ValueError(f"Unsupported size mode: {value.mode}")
    
    def _get_intrinsic_axis_size(self, axis: str) -> float:
        if axis == 'width':
            return self._node.compute_intrinsic_width()
        return self._node.compute_intrinsic_height()

    def _get_background_image_axis_size(self, axis: str) -> float:
        background_image = self._node.computed_styles.background_image.get()
        if not background_image:
            raise ValueError("Cannot use 'fit-background-image' on an element without a background image.")

        image = background_image.get_skia_image()
        if not image:
            raise ValueError(f"Background image for node could not be loaded: {background_image.path}")

        return getattr(image, axis)()

    def _get_parent_percent_axis_size(self, axis: str, factor: float) -> float:
        parent = self._node.parent
        if not parent:
            raise ValueError("Cannot use 'percent' size on a root element without a parent.")

        parent_size = getattr(parent.computed_styles, axis).get()
        if not parent_size or parent_size.mode == 'fit-content' or parent_size.mode == 'auto':
            raise ValueError("Cannot use 'percent' size if parent element has 'fit-content' size.")

        if axis == 'width':
            return parent.content_width * factor
        elif axis == 'height':
            return parent.content_height * factor
        
        raise ValueError(f"Unknown axis: {axis}")

    def _get_parent_available_axis_size_per_child(self, axis: str) -> float:
        parent = self._node.parent
        if not parent:
            raise ValueError("Cannot use 'fill-available' size on a root element without a parent.")

        parent_size_style = getattr(parent.computed_styles, axis).get()
        if not parent_size_style or parent_size_style.mode == 'fit-content' or parent_size_style.mode == 'auto':
            raise ValueError("Cannot use 'fill-available' size if parent element has 'fit-content' size.")
        
        # We just return the intrinsic size as a placeholder, this should be recalculated in the second phase
        return self._get_intrinsic_axis_size(axis)

    def _resolve_width_from_style(self) -> int:
        width = self._node.computed_styles.width.get()
        if not width:
            return self._node.compute_intrinsic_width()

        spacing = self._get_horizontal_spacing()
        box_width = self._get_axis_size(width, "width", spacing)
        return max(0, box_width)

    def _resolve_height_from_style(self) -> int:
        height = self._node.computed_styles.height.get()
        if not height:
            return self._node.compute_intrinsic_height()

        spacing = self._get_vertical_spacing()
        box_height = self._get_axis_size(height, "height", spacing)
        return max(0, box_height)

