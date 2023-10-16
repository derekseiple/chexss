"""
direction_utils.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from typing import List
from src.board.direction_iterator import DirectionDelta


def diagonal_direction_deltas() -> List[DirectionDelta]:
    """Returns the direction deltas for the six diagonal directions on the board."""
    return [
        DirectionDelta(2, -1),
        DirectionDelta(1, 1),
        DirectionDelta(-1, 2),
        DirectionDelta(-2, 1),
        DirectionDelta(-1, -1),
        DirectionDelta(1, -2)
    ]


def orthogonal_direction_deltas() -> List[DirectionDelta]:
    """Returns the direction deltas for the six orthogonal directions on the board."""
    return [
        DirectionDelta(1, 0),
        DirectionDelta(1, -1),
        DirectionDelta(0, 1),
        DirectionDelta(0, -1),
        DirectionDelta(-1, 0),
        DirectionDelta(-1, 1)
    ]


def all_direction_deltas() -> List[DirectionDelta]:
    """Returns the direction deltas for all twelve directions on the board."""
    return orthogonal_direction_deltas() + diagonal_direction_deltas()
