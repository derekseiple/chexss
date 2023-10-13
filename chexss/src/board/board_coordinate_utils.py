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
    col: int = coordinate.x + (2 * (dimension - 1))
    row: int = coordinate.y + dimension - 1
    return "{}{}".format(chr(ord('a') + col), row + 1)
