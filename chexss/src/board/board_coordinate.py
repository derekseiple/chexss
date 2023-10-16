"""
board_coordinate.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""


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

        # doubled width coordinates
        self._x = 2 * self._q + self._r
        self._y = self._r

    def __str__(self) -> str:
        return "(q: {}, r: {})".format(self._q, self._r)

    def __eq__(self, other: 'BoardCoordinate') -> bool:  # type: ignore [override]
        return (
            type(self) == type(other) and
            self._q == other.q and
            self._r == other.r
        )

    def __hash__(self) -> int:
        return hash((self._q, self._r))

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
