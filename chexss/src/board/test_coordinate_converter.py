"""
test_coordinate_converter.py
Copyright © 2025 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
import unittest
from src.board.board import Board
from src.board.coordinate_converter import CoordinateConverter


class TestCoordinateConverter(unittest.TestCase):

    def test_works(self):
        """We test that we can construct it and get the string representation back."""
        board = Board(6)
        convert = CoordinateConverter(6)
        for coord in board.coordinates:
            self.assertEqual(convert.algebraic_to_board(convert.board_to_algebraic(coord)), coord)

        board = Board(7)
        convert = CoordinateConverter(7)
        for coord in board.coordinates:
            self.assertEqual(convert.algebraic_to_board(convert.board_to_algebraic(coord)), coord)

        board = Board(8)
        convert = CoordinateConverter(6)
        for coord in board.coordinates:
            self.assertEqual(convert.algebraic_to_board(convert.board_to_algebraic(coord)), coord)
