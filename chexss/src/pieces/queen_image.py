"""
queen_image.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from textwrap import dedent
from io import BytesIO
from cairosvg import svg2png
from PIL import Image
from src.board.hex_meta import HexMeta


class QueenImage:
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
            The color of the queen. This must be a valid SVG color string.
        
        accent_color: str
            The color of the queen's accent. This must be a valid SVG color string.
        
        This will create a queen image with the given colors and the size will match the size of the HexMeta.
        """
        scale_factor = 0.9
        scaled_dim = round(float(meta.width) * scale_factor)
        png = svg2png(bytestring=self.__get_svg(main_color, accent_color), scale=(scaled_dim / 45.0))
        self._image = Image.new("RGBA", (meta.width, meta.height), (255, 255, 255, 0))
        offset = (round((meta.width - scaled_dim) / 2), round((meta.height - scaled_dim) / 2))
        self._image.paste(Image.open(BytesIO(png)), offset)

    @property
    def image(self) -> Image:
        """The Pillow image of the queen."""
        return self._image

    def __get_svg(self, main_color: str, accent_color: str) -> str:
        """Return the SVG string for the queen image.
        The SVG code was adapted from here: https://commons.wikimedia.org/wiki/Chess_pieces#/media/File:Chess_qlt45.svg
        """
        return dedent("""
            <?xml version="1.0" encoding="UTF-8" standalone="no"?>
            <svg xmlns="http://www.w3.org/2000/svg" width="45" height="45">
              <g style="fill:{0};stroke:{1};stroke-width:1.5;stroke-linejoin:round">
                <path d="M 9,26 C 17.5,24.5 30,24.5 36,26 L 38.5,13.5 L 31,25 L 30.7,10.9 L 25.5,24.5 L 22.5,10 L 19.5,24.5 L 14.3,10.9 L 14,25 L 6.5,13.5 L 9,26 z"/>
                <path d="M 9,26 C 9,28 10.5,28 11.5,30 C 12.5,31.5 12.5,31 12,33.5 C 10.5,34.5 11,36 11,36 C 9.5,37.5 11,38.5 11,38.5 C 17.5,39.5 27.5,39.5 34,38.5 C 34,38.5 35.5,37.5 34,36 C 34,36 34.5,34.5 33,33.5 C 32.5,31 32.5,31.5 33.5,30 C 34.5,28 36,28 36,26 C 27.5,24.5 17.5,24.5 9,26 z"/>
                <path d="M 11.5,30 C 15,29 30,29 33.5,30" style="fill:none"/>
                <path d="M 12,33.5 C 18,32.5 27,32.5 33,33.5" style="fill:none"/>
                <circle cx="6" cy="12" r="2" />
                <circle cx="14" cy="9" r="2" />
                <circle cx="22.5" cy="8" r="2" />
                <circle cx="31" cy="9" r="2" />
                <circle cx="39" cy="12" r="2" />
              </g>
            </svg>
            """).strip("\n").format(main_color, accent_color)
