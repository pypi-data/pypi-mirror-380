import skia
from ..models import FontSmoothing
from ..models import CropMode
from .image_processor import ImageProcessor
from .vector_image_processor import VectorImageProcessor
from ..models import RenderProps
from ..bitmap_image import BitmapImage
from ..vector_image import VectorImage
from ..nodes import Node

class Renderer:

    def render_as_bitmap(self, root: Node, crop_mode: CropMode, font_smoothing: FontSmoothing, scale_factor: float = 1.0) -> BitmapImage:
        """Renders the nodes with the given builders, generating a bitmap image."""
        root.prepare_tree_for_rendering(RenderProps(False, crop_mode, font_smoothing))

        canvas_bounds = root.paint_bounds
        
        # Calculate actual rendering dimensions based on scale factor
        render_width = int(canvas_bounds.width() * scale_factor)
        render_height = int(canvas_bounds.height() * scale_factor)
        
        image_info = skia.ImageInfo.MakeN32Premul(render_width, render_height)
        surface = skia.Surface(image_info)
        canvas = surface.getCanvas()
        canvas.clear(skia.ColorTRANSPARENT)
        
        # Scale the canvas by the scale factor
        canvas.scale(scale_factor, scale_factor)
        canvas.translate(-canvas_bounds.left(), -canvas_bounds.top())

        root.paint(canvas)
        del canvas
        final_image = surface.makeImageSnapshot()
        return ImageProcessor().process(root, final_image, crop_mode)
    
    def render_as_svg(self, root: Node, embed_fonts: bool) -> VectorImage:
        """Renders the text with the given builders, generating a vector image."""
        # If support shadows in the near future, we should use CropMode.NONE.
        root.prepare_tree_for_rendering(RenderProps(True, CropMode.CONTENT_BOX, FontSmoothing.SUBPIXEL))

        canvas_bounds = root.paint_bounds
        stream = skia.DynamicMemoryWStream()
        canvas = skia.SVGCanvas.Make(canvas_bounds, stream)
        canvas.clear(skia.ColorTRANSPARENT)
        canvas.translate(-canvas_bounds.left(), -canvas_bounds.top())

        root.paint(canvas)
        del canvas
        return VectorImageProcessor().process(stream, embed_fonts, root)
