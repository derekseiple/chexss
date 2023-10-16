"""
board_coordinate_utils.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from src.board.board_coordinate import BoardCoordinate


def get_algebraic_notation(dimension: int, coordinate: BoardCoordinate) -> str:
    """Returns the algebraic notation for the given coordinate. The value depends on the dimension of the board.

    Parameters
    ----------
    dimension: int
        The dimension of the board, ie the number of hexes on a side.

    coordinate: BoardCoordinate
        The coordinate to get the algebraic notation for.
    """
    # We convert from the doubled width coordinate system to the equivalent algebraic notation. The difference is that
    # the y-coordinate increases from top to bottom, but in the algebraic notation it increases from bottom to top, so
    # we need to flip the y-coordinate.
    col: int = coordinate.x + (2 * (dimension - 1))
    row: int = dimension - 1 - coordinate.y
    return "{}{}".format(chr(ord('a') + col), row + 1)
