"""
board_coordinates.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from typing import List


class BoardCoordinate:
    """This class represents a coordinate on the board. There are several different coordinate systems that can be used
    to represent a hex on a board. Many are discussed here: https://www.redblobgames.com/grids/hexagons/. We will use
    both the cube and rectangular coordinate systems. The cube coordinate system is useful for calculating distances and
    easily finding where pieces can move to. The rectangular coordinate system is useful for drawing the board. We wrap
    both of these coordinate systems in this class, so we can easily convert between them as needed depending on the
    use case.
    """

    def __init__(
        self,
        q: int,
        r: int
    ) -> None:
        """Constructor.

        Parameters
        ----------
        q: int
            The q coordinate of the hex.

        r: int
            The r coordinate of the hex.
        """
        # cube coordinates
        self._q = q
        self._r = r
        self._s = -q - r

        # rectangular coordinates
        self._x = 2 * self._q + self._r
        self._y = self._r

    @property
    def q(self) -> int:
        return self._q

    @property
    def r(self) -> int:
        return self._r
    
    @property
    def s(self) -> int:
        return self._s
    
    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y


class BoardCoordinates:
    """This class represents all of the coordinates on the board. The coordinates property is a list of all the valid
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
        for q in range(-self._dimension + 1, self._dimension):
            for r in range(-self._dimension + 1, self._dimension):
                coord = BoardCoordinate(q, r)
                if (abs(coord.s) < self._dimension):
                    self._coordinates.append(coord)

    @property
    def coordinates(self) -> List[BoardCoordinate]:
        return self._coordinates
