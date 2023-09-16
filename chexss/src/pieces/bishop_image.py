"""
bishop_image.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from textwrap import dedent
from io import BytesIO
from cairosvg import svg2png
from PIL import Image
from src.hex_meta import HexMeta


class BishopImage:
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
            The color of the bishop. This must be a valid SVG color string.
        
        accent_color: str
            The color of the bishop's accent. This must be a valid SVG color string.
        
        This will create a bishop image with the given colors and the size will match the size of the HexMeta.
        """
        scale_factor = 0.85
        scaled_dim = round(float(meta.width) * scale_factor)
        png = svg2png(bytestring=self.__get_svg(main_color, accent_color), scale=(scaled_dim / 45.0))
        self._image = Image.new("RGBA", (meta.width, meta.height), (255, 255, 255, 0))
        offset = (round((meta.width - scaled_dim) / 2), round((meta.height - scaled_dim) / 2))
        self._image.paste(Image.open(BytesIO(png)), offset)

    @property
    def image(self) -> Image:
        """The Pillow image of the bishop."""
        return self._image

    def __get_svg(self, main_color: str, accent_color: str) -> str:
        """Return the SVG string for the bishop image.
        The SVG code was adapted from here: https://commons.wikimedia.org/wiki/Chess_pieces#/media/File:Chess_blt45.svg
        """
        return dedent("""
            <?xml version="1.0" encoding="UTF-8" standalone="no"?>
            <svg xmlns="http://www.w3.org/2000/svg" width="45" height="45">
              <g style="opacity:1; fill:none; fill-rule:evenodd; fill-opacity:1; stroke:{1}; stroke-width:1.5; stroke-linecap:round; stroke-linejoin:round; stroke-miterlimit:4; stroke-dasharray:none; stroke-opacity:1;" transform="translate(0,0.6)">
                <g style="fill:{0}; stroke:{1}; stroke-linecap:butt;">
                  <path d="M 9,36 C 12.39,35.03 19.11,36.43 22.5,34 C 25.89,36.43 32.61,35.03 36,36 C 36,36 37.65,36.54 39,38 C 38.32,38.97 37.35,38.99 36,38.5 C 32.61,37.53 25.89,38.96 22.5,37.5 C 19.11,38.96 12.39,37.53 9,38.5 C 7.65,38.99 6.68,38.97 6,38 C 7.35,36.54 9,36 9,36 z"/>
                  <path d="M 15,32 C 17.5,34.5 27.5,34.5 30,32 C 30.5,30.5 30,30 30,30 C 30,27.5 27.5,26 27.5,26 C 33,24.5 33.5,14.5 22.5,10.5 C 11.5,14.5 12,24.5 17.5,26 C 17.5,26 15,27.5 15,30 C 15,30 14.5,30.5 15,32 z"/>
                  <path d="M 25 8 A 2.5 2.5 0 1 1  20,8 A 2.5 2.5 0 1 1  25 8 z"/>
                </g>
                <g style="fill:none; stroke:{1}; stroke-linejoin:miter;">
                  <path d="M 17.5,26 L 27.5,26 M 15,30 L 30,30"/>
                  <path d="M 22.5,15.5 L 20,18 L 22.5,20.5 L 25,18 Z"/>
                </g>
              </g>
            </svg>
            """).strip("\n").format(main_color, accent_color)
