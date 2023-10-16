"""
direction_iterator.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from src.board.board_coordinate import BoardCoordinate


class DirectionDelta:
    """This class is used to represent a direction on the board. It is used to iterate through the board in a given
    direction. The direction is defined by specifying how much the q and r coordinates change when moving in that."""

    def __init__(self, q: int, r: int) -> None:
        self.q_: int = q
        self.r_: int = r

    @property
    def q(self) -> int:
        return self.q_

    @property
    def r(self) -> int:
        return self.r_


class DirectionIterator:
    """This class is used to iterate through the board in a given direction. Many pieces can move in straight lines
    until that path is blocked. This class give us a clean way to traverse a particular direction on the board."""

    def __init__(
        self,
        coord: BoardCoordinate,
        direction: DirectionDelta,
    ) -> None:
        self.coord_: BoardCoordinate = coord
        self.direction_: DirectionDelta = direction

    def next(self) -> BoardCoordinate:
        self.coord_ = BoardCoordinate(
            self.coord_.q + self.direction_.q,
            self.coord_.r + self.direction_.r
        )
        return self.coord_
