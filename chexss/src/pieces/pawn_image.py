"""
pawn_image.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from textwrap import dedent
from io import BytesIO
from cairosvg import svg2png
from PIL import Image
from src.board.hex_meta import HexMeta


class PawnImage:
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
            The color of the pawn. This must be a valid SVG color string.
        
        accent_color: str
            The color of the pawn's accent. This must be a valid SVG color string.
        
        This will create a pawn image with the given colors and the size will match the size of the HexMeta.
        """
        scale_factor = 0.9
        scaled_dim = round(float(meta.width) * scale_factor)
        png = svg2png(bytestring=self.__get_svg(main_color, accent_color), scale=(scaled_dim / 45.0))
        self._image = Image.new("RGBA", (meta.width, meta.height), (255, 255, 255, 0))
        offset = (round((meta.width - scaled_dim) / 2), round((meta.height - scaled_dim) / 2))
        self._image.paste(Image.open(BytesIO(png)), offset)

    @property
    def image(self) -> Image:
        """The Pillow image of the pawn."""
        return self._image

    def __get_svg(self, main_color: str, accent_color: str) -> str:
        """Return the SVG string for the pawn image.
        The SVG code was adapted from here: https://commons.wikimedia.org/wiki/Chess_pieces#/media/File:Chess_plt45.svg
        """
        return dedent("""
            <?xml version="1.0" encoding="UTF-8" standalone="no"?>
            <svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="45" height="45">
              <path
                d="m 22.5,9 c -2.21,0 -4,1.79 -4,4 0,0.89 0.29,1.71 0.78,2.38 C 17.33,16.5 16,18.59 16,21 c 0,2.03 0.94,3.84 2.41,5.03 C 15.41,27.09 11,31.58 11,39.5 H 34 C 34,31.58 29.59,27.09 26.59,26.03 28.06,24.84 29,23.03 29,21 29,18.59 27.67,16.5 25.72,15.38 26.21,14.71 26.5,13.89 26.5,13 c 0,-2.21 -1.79,-4 -4,-4 z"
                style="opacity:1; fill:{0}; fill-opacity:1; fill-rule:nonzero; stroke:{1}; stroke-width:1.5; stroke-linecap:round; stroke-linejoin:miter; stroke-miterlimit:4; stroke-dasharray:none; stroke-opacity:1;"/>
            </svg>
            """).strip("\n").format(main_color, accent_color)
