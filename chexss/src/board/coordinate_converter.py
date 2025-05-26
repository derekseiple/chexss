"""
coordinate_converter.py
Copyright © 2025 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from src.board.algebraic_coordinate import AlgebraicCoordinate
from src.board.board_coordinate import BoardCoordinate


class CoordinateConverter:
    """You can convert between algebraic notation and a board coordinates but they are not the same thing. The reason
    for this is that the algebraic notation is dependent on the dimension of the board, while the board coordinates
    are not. This class handles the conversion between the two given the dimension of the board it is initialized with.
    """

    def __init__(self, dimension: int) -> None:
        """Constructor.

        Parameters
        ----------
        dimension : int
            The dimension of the board, ie the number of hexes on a side.
        """
        self._dimension = dimension

    def algebraic_to_board(self, algebraic: AlgebraicCoordinate) -> BoardCoordinate:
        """Convert an algebraic coordinate to a board coordinate.

        Parameters
        ----------
        algebraic : AlgebraicCoordinate
            The algebraic coordinate to convert.
        """
        # We convert from algebraic notation to the doubled width coordinate system. The difference is
        # that the y-coordinate increases from bottom to top in algebraic notation, but in the board coordinates
        # it increases from top to bottom, so we need to flip the y-coordinate.
        x: int = algebraic.column - (2 * (self._dimension - 1))
        y: int = self._dimension - 1 - algebraic.row
        return BoardCoordinate((x - y) // 2, y)

    def board_to_algebraic(self, board: BoardCoordinate) -> AlgebraicCoordinate:
        """Convert a board coordinate to an algebraic coordinate.

        Parameters
        ----------
        board : BoardCoordinate
            The board coordinate to convert.
        """
        # We convert from the doubled width coordinate system to the equivalent algebraic notation. The difference is
        # that the y-coordinate increases from top to bottom, but in the algebraic notation it increases from bottom to
        # top, so we need to flip the y-coordinate.
        col: int = board.x + (2 * (self._dimension - 1))
        row: int = self._dimension - 1 - board.y
        return AlgebraicCoordinate(col, row)
