"""
knight_image.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from textwrap import dedent
from io import BytesIO
from cairosvg import svg2png
from PIL import Image
from src.board.hex_meta import HexMeta


class KnightImage:
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
            The color of the knight. This must be a valid SVG color string.

        accent_color: str
            The color of the knight's accent. This must be a valid SVG color string.

        This will create a knight image with the given colors and the size will match the size of the HexMeta.
        """
        scale_factor = 0.9
        scaled_dim = round(float(meta.width) * scale_factor)
        png = svg2png(bytestring=self.__get_svg(main_color, accent_color), scale=(scaled_dim / 45.0))
        self._image = Image.new("RGBA", (meta.width, meta.height), (255, 255, 255, 0))
        offset = (round((meta.width - scaled_dim) / 2), round((meta.height - scaled_dim) / 2))
        self._image.paste(Image.open(BytesIO(png)), offset)

    @property
    def image(self) -> Image:
        """The Pillow image of the knight."""
        return self._image

    def __get_svg(self, main_color: str, accent_color: str) -> str:
        """Return the SVG string for the knight image.
        The SVG code was adapted from here: https://commons.wikimedia.org/wiki/Chess_pieces#/media/File:Chess_nlt45.svg
        """
        return dedent("""
            <?xml version="1.0" encoding="UTF-8" standalone="no"?>
            <svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="45" height="45">
              <g style="opacity:1; fill:none; fill-opacity:1; fill-rule:evenodd; stroke:{1}; stroke-width:1.5;
                  stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4; stroke-dasharray:none;
                  stroke-opacity:1;" transform="translate(0,0.3)">
                <path
                  d="M 22,10 C 32.5,11 38.5,18 38,39 L 15,39 C 15,30 25,32.5 23,18"
                  style="fill:{0}; stroke:{1};" />
                <path
                  d="M 24,18 C 24.38,20.91 18.45,25.37 16,27 C 13,29 13.18,31.34 11,31 C 9.958,30.06 12.41,27.96 11,28
                      C 10,28 11.19,29.23 10,30 C 9,30 5.997,31 6,26 C 6,24 12,14 12,14 C 12,14 13.89,12.1 14,10.5
                      C 13.27,9.506 13.5,8.5 13.5,7.5 C 14.5,6.5 16.5,10 16.5,10 L 18.5,10 C 18.5,10 19.28,8.008 21,7
                      C 22,7 22,10 22,10"
                  style="fill:{0}; stroke:{1};" />
                <path
                  d="M 9.5 25.5 A 0.5 0.5 0 1 1 8.5,25.5 A 0.5 0.5 0 1 1 9.5 25.5 z"
                  style="fill:{1}; stroke:{1};" />
                <path
                  d="M 15 15.5 A 0.5 1.5 0 1 1  14,15.5 A 0.5 1.5 0 1 1  15 15.5 z"
                  transform="matrix(0.866,0.5,-0.5,0.866,9.693,-5.173)"
                  style="fill:{1}; stroke:{1};" />
              </g>
            </svg>
            """).strip("\n").format(main_color, accent_color)
