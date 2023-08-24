"""
board_coordinates.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from typing import List


class BoardCoordinate:
    """This class represents a coordinate on the board. The coordinate is represented by a column and a row. Since the
    board is hexagonal, the column and row are not independent, so not every combination of column and row is valid.

    This class should not be instantiated directly. Instead, use the BoardCoordinates class to get a list of valid
    coordinates.
    """

    def __init__(self, col: int, row: int) -> None:
        self._col = col
        self._row = row
    
    @property
    def col(self) -> int:
        return self._col
    
    @property
    def row(self) -> int:
        return self._row


class BoardCoordinates:
    """This class represents the coordinates on the board. The coordinates property is a list of all the valid
    coordinates for the given board size.
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
        for col in range(4 * self._dimension - 3):
            for row in range(2 * self._dimension - 1):
                if (self.__is_valid_coordinate(col, row)):
                    self._coordinates.append(BoardCoordinate(col, row))

    def __is_valid_coordinate(self, col: int, row: int) -> bool:
        """Returns True if the given coordinate is valid coordinate on the board, False otherwise."""
        return (
            # The dimension are valid if the sum of the coordinates is even.
            ((col + row) % 2) == ((self._dimension - 1) % 2) and
            # The following four conditions trim the board to a hexagon.
            col + row >= self._dimension - 1 and # trim bottom left
            col + row <= 5 * (self._dimension - 1) and # trim top right
            col - row >= -(self._dimension - 1) and # trim top left
            col - row <= 3 * (self._dimension - 1) # trim bottom right
        )

    @property
    def coordinates(self) -> List[BoardCoordinate]:
        return self._coordinates
