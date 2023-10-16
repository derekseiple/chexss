"""
test_direction_iterator.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
import unittest
from src.board.board_coordinate import BoardCoordinate
from src.board.direction_iterator import DirectionIterator, DirectionDelta


class TestDirectionIterator(unittest.TestCase):

    def test_can_iterate_diagonally(self):
        """We test that we can iterate diagonally."""
        coord = BoardCoordinate(6, -4)
        direction = DirectionDelta(-1, 2)
        it = DirectionIterator(coord, direction)

        expected_coords = [
            BoardCoordinate(5, -2),
            BoardCoordinate(4, 0),
            BoardCoordinate(3, 2),
            BoardCoordinate(2, 4)
        ]

        for i in range(len(expected_coords)):
            self.assertEqual(it.next(), expected_coords[i])

    def test_can_iterate_orthogonally(self):
        """We test that we can iterate orthogonally."""
        coord = BoardCoordinate(2, -3)
        direction = DirectionDelta(-1, 0)
        it = DirectionIterator(coord, direction)

        expected_coords = [
            BoardCoordinate(1, -3),
            BoardCoordinate(0, -3),
            BoardCoordinate(-1, -3),
            BoardCoordinate(-2, -3),
            BoardCoordinate(-3, -3)
        ]

        for i in range(len(expected_coords)):
            self.assertEqual(it.next(), expected_coords[i])
