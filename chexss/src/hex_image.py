"""
hex_image.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from PIL import Image, ImageDraw
from src.hex_meta import HexMeta
from src.rgb_color import RgbColor


class HexImage:
    """This class wraps a Pillow image of a hex on the Chexss board. The image is drawn with a transparent background
    so they can be composed together to form the board.
    """

    def __init__(
        self,
        meta: HexMeta,
        color: RgbColor
    ) -> None:
        """Constructor.

        Parameters
        ----------
        meta: HexMeta
            The metadata about the hex.

        color: RgbColor
            The color of the hex.
        """
        self._image = Image.new("RGBA", (meta.width, meta.height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(self._image)
        draw.polygon(meta.coords, fill=color.rgb, outline=color.rgb)

    @property
    def image(self) -> Image:
        """The Pillow image of the hex."""
        return self._image
