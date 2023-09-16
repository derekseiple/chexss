"""
board_image.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from PIL import Image
from src.board.board_coordinates import BoardCoordinates
from src.board.board_colors import BoardColors
from src.board.hex_image import HexImage
from src.board.hex_meta import HexMeta
from src.board.drawer_utils import board_coordinate_image_location


class BoardImage:
    """This class wraps a Pillow image of a Chexss board of a given size. This uses the HexMeta information along with
    the board dimensions to draw the board.
    """

    def __init__(
        self,
        dimension: int,
        hex_meta: HexMeta,
        board_colors: BoardColors = BoardColors.CreateDefault()
    ) -> None:
        """Constructor.

        Parameters
        ----------
        dimension: int
            The dimension of the board, ie the number of hexes on a side.

        hex_meta: HexMeta
            The metadata about the hexes.

        board_colors: BoardColors
            The color of the hexes used for the board.
        """
        self._dimension = dimension
        self._hex_meta = hex_meta
        self._hexes = [
            HexImage(self._hex_meta, board_colors.white),
            HexImage(self._hex_meta, board_colors.silver),
            HexImage(self._hex_meta, board_colors.black)
        ]

        # Create the image.
        width: int = hex_meta.width * (2 * self._dimension - 1)
        height: int = int(hex_meta.height / 2) * (3 * self._dimension - 1)
        self._image = Image.new("RGBA", (width, height), (255, 255, 255, 0))

        # Draw the board.
        board_coords = BoardCoordinates(self._dimension)
        for coord in board_coords.coordinates:
            self._image.alpha_composite(
                self.__get_hex_image(coord.x),
                board_coordinate_image_location(self._dimension, coord, hex_meta)
            )

    def __get_hex_image(self, col: int) -> Image:
        """Depending on the size of the board, and column each hex will be a different color. This method returns the
        hex image needed for the given column. This is done in a way that the center hex will be "black", and the colors
        alternate from left to right as "white", "silver", "black".
        """
        return self._hexes[(-col + 2) % 3].image

    @property
    def dimension(self) -> int:
        """The dimension of the board, ie the number of hexes on a side."""
        return self._dimension

    @property
    def hex_meta(self) -> HexMeta:
        """The metadata about the hexes."""
        return self._hex_meta

    @property
    def image(self) -> Image:
        """The Pillow image of the board."""
        return self._image
