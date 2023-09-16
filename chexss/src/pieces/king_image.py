"""
king_image.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from textwrap import dedent
from io import BytesIO
from cairosvg import svg2png
from PIL import Image
from src.board.hex_meta import HexMeta


class KingImage:
    def __init__(
            self,
            meta: HexMeta,
            main_color: str,
            accent_color: str
        ) -> None:
        """Constructor.

        Parameters
        ----------
        meta: HexMeta
            Provides the information about the hexagon size so we can scale the image appropriately.
        
        main_color: str
            The color of the king. This must be a valid SVG color string.
        
        accent_color: str
            The color of the king's accent. This must be a valid SVG color string.
        
        This will create a king image with the given colors and the size will match the size of the HexMeta.
        """
        scale_factor = 1.0
        scaled_dim = round(float(meta.width) * scale_factor)
        png = svg2png(bytestring=self.__get_svg(main_color, accent_color), scale=(scaled_dim / 45.0))
        self._image = Image.new("RGBA", (meta.width, meta.height), (255, 255, 255, 0))
        offset = (round((meta.width - scaled_dim) / 2), round((meta.height - scaled_dim) / 2))
        self._image.paste(Image.open(BytesIO(png)), offset)

    @property
    def image(self) -> Image:
        """The Pillow image of the king."""
        return self._image

    def __get_svg(self, main_color: str, accent_color: str) -> str:
        """Return the SVG string for the king image.
        The SVG code was adapted from here: https://commons.wikimedia.org/wiki/Chess_pieces#/media/File:Chess_klt45.svg
        """
        return dedent("""
            <?xml version="1.0" encoding="UTF-8" standalone="no"?>
            <svg xmlns="http://www.w3.org/2000/svg" width="45" height="45">
              <g fill="{0}" fill-rule="evenodd" stroke="{1}" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5">
                <path stroke-linejoin="miter" d="M22.5 11.63 L25 8 L22.5 5.63 L20 8 Z"/>
                <path stroke-linecap="butt" stroke-linejoin="miter" d="M22.5 25s4.5-7.5 3-10.5c0 0-1-2.5-3-2.5s-3 2.5-3 2.5c-1.5 3 3 10.5 3 10.5"/>
                <path d="M12.5 37c5.5 3.5 14.5 3.5 20 0v-7s9-4.5 6-10.5c-4-6.5-13.5-3.5-16 4V27v-3.5c-2.5-7.5-12-10.5-16-4-3 6 6 10.5 6 10.5v7"/>
                <path d="M12.5 30c5.5-3 14.5-3 20 0m-20 3.5c5.5-3 14.5-3 20 0m-20 3.5c5.5-3 14.5-3 20 0"/>
              </g>
            </svg>
            """).strip("\n").format(main_color, accent_color)
