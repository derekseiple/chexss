"""
drawer_utils.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from typing import Tuple
from src.board.board_coordinate import BoardCoordinate
from src.board.hex_meta import HexMeta


def board_coordinate_image_location(
    dimension: int,
    coordinate: BoardCoordinate,
    hex_meta: HexMeta
) -> Tuple[int, int]:
    """Returns the x and y offset of the given board coordinate on the board image. This allows us to draw the hex image
    at the correct location on the board image, and will also allow us to draw other images at the correct location,
    like the piece images.

    Parameters
    ----------
    dimension: int
        The dimension of the board, ie the number of hexes on a side.

    coordinate: BoardCoordinate
        The coordinate on the board to draw the image at.

    hex_meta: HexMeta
        The metadata about the hexes.
    """

    # The BoardCoordinate has values of 0 at the center of the board, but the image coordinates have values of 0 at the
    # bottom left of the board. So we need to shift the coordinates according to the dimension of the board.
    col: int = coordinate.x + (2 * (dimension - 1))
    row: int = coordinate.y + dimension - 1

    return (
        col * hex_meta.horizontal_step,
        row * hex_meta.vertical_step
    )
