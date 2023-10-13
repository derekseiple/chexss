"""
board.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from typing import List
from src.board.board_coordinate import BoardCoordinate


class Board:
    """This class represents the board. The coordinates property is a list of all the valid coordinates for the given
    board size.
    """

    def __init__(self, dimension: int) -> None:
        """Constructor.

        Parameters
        ----------
        dimension: int
            The dimension of the board, ie the number of hexes on a side.
        """
        self._dimension = dimension

        # Generate the valid coordinates for the board.
        self._coordinates = []
        for q in range(-self._dimension + 1, self._dimension):
            for r in range(-self._dimension + 1, self._dimension):
                coord = BoardCoordinate(q, r)
                if (abs(coord.s) < self._dimension):
                    self._coordinates.append(coord)

    def is_valid_coordinate(self, coord: BoardCoordinate) -> bool:
        """Returns true if the coordinate is a valid coordinate on the board.

        Parameters
        ----------
        coord: BoardCoordinate
            The coordinate to check.

        Returns
        -------
        bool
            True if the coordinate is a valid coordinate on the board.
        """
        return (
            abs(coord.q) < self._dimension and
            abs(coord.r) < self._dimension and
            abs(coord.s) < self._dimension
        )

    @property
    def dimension(self) -> int:
        return self._dimension

    @property
    def coordinates(self) -> List[BoardCoordinate]:
        return self._coordinates
