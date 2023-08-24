"""
board_image.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from PIL import Image
from src.board_coordinates import BoardCoordinates
from src.board_colors import BoardColors
from src.hex_image import HexImage
from src.hex_meta import HexMeta


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
        self.__set_hexes(board_colors)

        # Create the image.
        width: int = hex_meta.width * (2 * dimension - 1)
        height: int = int(hex_meta.height / 2) * (3 * dimension - 1)
        self._image = Image.new("RGBA", (width, height), (255, 255, 255, 0))

        # Draw the board.
        board_coords = BoardCoordinates(dimension)
        for coord in board_coords.coordinates:
            # The board coordinates go from bottom to top, but the image coordinates go from top to bottom. So we need
            # to flip the row coordinate.
            offset = (coord.col * hex_meta.horizontal_step, (2 * (dimension - 1) - coord.row) * hex_meta.vertical_step)
            self._image.alpha_composite(self.__get_hex_image(coord.col), offset)

    def __set_hexes(self, board_colors: BoardColors) -> None:
        self._hexes = [
            HexImage(self._hex_meta, board_colors.white),
            HexImage(self._hex_meta, board_colors.silver),
            HexImage(self._hex_meta, board_colors.black)
        ]
        self._start_hex_idx = -(self._dimension % 3)

    def __get_hex_image(self, col: int) -> Image:
        """Depending on the size of the board, and column each hex will be a different color. This method returns the
        hex image needed for the given column.
        """
        return self._hexes[(self._start_hex_idx - col) % 3].image

    @property
    def image(self) -> Image:
        """The Pillow image of the board."""
        return self._image
