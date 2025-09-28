from __future__ import annotations
from typing import Literal, Optional
import skia
import numpy as np
from .models import Box, RenderNode
import os

class BitmapImage:
    """A wrapper around a rendered raster image.

    This class holds the pixel data from a rendered image and provides
    convenient methods to save it to a file or convert it to other common
    formats like NumPy arrays or Pillow (PIL) Images.

    Objects of this class are typically created by calling `Canvas.render()`.

    Example:
        ```python
        # Assuming 'canvas' is a pre-configured Canvas object
        image = canvas.render("Hello World")

        # Save the image to a file
        image.save("output.png")

        # Get a NumPy array for use with OpenCV or other libraries
        import cv2
        cv2_image = image.to_numpy()
        cv2.imshow("Render", cv2_image)
        cv2.waitKey(0)
        ```

    Attributes:
        content_box (Box): The bounding box of the content (text + padding),
            relative to the image's top-left corner.
        width (int): The total width of the image in pixels.
        height (int): The total height of the image in pixels.
        skia_image (skia.Image): The underlying raw `skia.Image` object for
            advanced use cases.
        render_tree (RenderNode): The hierarchical structure of rendered nodes
            with their bounds information.
    """

    def __init__(self, skia_image: skia.Image, content_box: Box, render_tree: Optional[RenderNode] = None):
        """Initializes the Image wrapper.

        Note:
            This constructor is intended for internal use by the library,
            typically called from `Canvas.render()`.

        Args:
            skia_image: The underlying `skia.Image` object.
            content_box: The calculated bounding box of the content area.
            render_tree: The hierarchical structure of rendered nodes with bounds.
        """
        self._skia_image = skia_image
        self._content_box = content_box
        self._render_tree = render_tree

    @property
    def content_box(self) -> Box:
        """Gets the bounding box of the content area."""
        return self._content_box

    @property
    def width(self) -> int:
        """Gets the width of the image in pixels."""
        return self._skia_image.width()

    @property
    def height(self) -> int:
        """Gets the height of the image in pixels."""
        return self._skia_image.height()

    @property
    def skia_image(self) -> skia.Image:
        """Gets the raw, underlying `skia.Image` object."""
        return self._skia_image

    @property
    def render_tree(self) -> Optional[RenderNode]:
        """Gets the hierarchical structure of rendered nodes with bounds."""
        return self._render_tree

    def to_bytes(self) -> bytes:
        """Returns the raw pixel data as a byte string.

        The format of the byte string is 32-bit BGRA, with 8 bits per
        component.

        Returns:
            A byte string containing the raw pixel data.
        """
        return self._skia_image.tobytes()

    def to_numpy(self, mode: Literal['RGBA', 'BGRA', 'RGB', 'Grayscale'] = 'RGBA') -> np.ndarray:
        """Converts the image to a NumPy array in the specified channel order.

        Args:
            mode (Literal['RGBA', 'BGRA', 'RGB', 'Grayscale'], optional):
                The desired channel order or format for the output array.
                Defaults to 'RGBA', the most common format for image processing.
                - 'RGBA': Red, Green, Blue, Alpha.
                - 'BGRA': Blue, Green, Red, Alpha. Compatible with OpenCV.
                - 'RGB': Red, Green, Blue. Alpha channel is discarded.
                - 'Grayscale': Converts the image to a single-channel grayscale.

        Returns:
            A NumPy array representing the image. The shape will be
            (height, width, 4) for RGBA/BGRA, (height, width, 3) for RGB,
            and (height, width) for Grayscale.
        """
        bgra_array = np.frombuffer(self.to_bytes(), dtype=np.uint8).reshape(
            (self.height, self.width, 4)
        )
        mode = mode.lower()

        if mode == 'rgba':
            return bgra_array[:, :, [2, 1, 0, 3]]  # Swap R and B channels

        if mode == 'bgra':
            return bgra_array

        if mode == 'rgb':
            return bgra_array[:, :, [2, 1, 0]]

        if mode == 'grayscale':
            rgb_array = bgra_array[:, :, [2, 1, 0]]
            return np.dot(rgb_array[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)

        raise ValueError(f"Unsupported mode: '{mode}'. Expected 'RGBA', 'BGRA', 'RGB', or 'Grayscale'.")

    def to_pillow(self) -> "PillowImage":
        """Converts the image to a Pillow (PIL) Image object.

        The returned Pillow Image will be in 'RGBA' mode.

        Returns:
            A `PIL.Image.Image` object.

        Raises:
            ImportError: If the Pillow library is not installed.
        """
        try:
            from PIL import Image as PillowImage
        except ImportError:
            raise ImportError(
                "Pillow is not installed. Please install it with 'pip install Pillow'."
            )

        rgba_array = self.to_numpy('RGBA')

        # Skia returns premultiplied alpha, but Pillow expects straight alpha
        # We need to unpremultiply the RGB channels
        alpha = rgba_array[:, :, 3:4].astype(np.float32)
        rgb = rgba_array[:, :, :3].astype(np.float32)
        alpha_nonzero = np.maximum(alpha, 1)
        rgb_unpremultiplied = np.divide(rgb * 255, alpha_nonzero, out=rgb, where=alpha > 0)

        result = np.concatenate([
            np.clip(rgb_unpremultiplied, 0, 255).astype(np.uint8),
            rgba_array[:, :, 3:4]
        ], axis=2)

        return PillowImage.fromarray(result, mode='RGBA')

    def save(self, output_path: str, quality: int = 100) -> None:
        """Saves the image to a file.

        The output format is inferred from the file extension. Supported
        formats are PNG, JPEG, and WebP. Defaults to PNG if the extension
        is unknown.

        Args:
            output_path: The path to save the output image (e.g., 'image.png').
            quality: An integer from 0 to 100 indicating image quality. This
                is only used for lossy formats like JPEG and WebP. It is
                ignored for PNG.

        Raises:
            RuntimeError: If Skia fails to encode the image to the specified
                format.
            IOError: If there is an error writing the file to disk.
        """
        ext = os.path.splitext(output_path)[1].lower()
        format_map = {
            ".png": skia.EncodedImageFormat.kPNG,
            ".jpg": skia.EncodedImageFormat.kJPEG,
            ".jpeg": skia.EncodedImageFormat.kJPEG,
            ".webp": skia.EncodedImageFormat.kWEBP,
        }
        # Default to PNG if the format is not recognized
        fmt = format_map.get(ext, skia.EncodedImageFormat.kPNG)

        data = self._skia_image.encodeToData(fmt, quality)
        if data is None:
            raise RuntimeError(f"Failed to encode image to format '{fmt}'")

        with open(output_path, "wb") as f:
            f.write(data.bytes())

    def show(self) -> None:
        """Displays the image using the default Pillow viewer.

        This method is useful for debugging in scripts and interactive
        environments like Jupyter notebooks.

        Raises:
            ImportError: If the Pillow library is not installed.
        """
        self.to_pillow().show()
