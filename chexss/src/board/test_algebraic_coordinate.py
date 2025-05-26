"""
test_algebraic_coordinate.py
Copyright © 2025 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
import unittest
from src.board.algebraic_coordinate import AlgebraicCoordinate


class TestAlgebraicCoordinate(unittest.TestCase):

    def test_works(self):
        """We test that we can construct it and get the string representation back."""
        coords = [
            "a1",
            "a2",
            "b1",
            "b2",
            "g17",
            "ac1",
            "azs543",
            "zz1000"
        ]
        for coord in coords:
            self.assertEqual(str(AlgebraicCoordinate.from_string(coord)), coord)

    def test_from_string(self):
        """We test that we can create an AlgebraicCoordinate from a string."""
        self.assertEqual(AlgebraicCoordinate.from_string("a1"), AlgebraicCoordinate(0, 0))
        self.assertEqual(AlgebraicCoordinate.from_string("a2"), AlgebraicCoordinate(0, 1))
        self.assertEqual(AlgebraicCoordinate.from_string("b1"), AlgebraicCoordinate(1, 0))
        self.assertEqual(AlgebraicCoordinate.from_string("b2"), AlgebraicCoordinate(1, 1))
        self.assertEqual(AlgebraicCoordinate.from_string("g17"), AlgebraicCoordinate(6, 16))
        self.assertEqual(AlgebraicCoordinate.from_string("ac1"), AlgebraicCoordinate(28, 0))
        self.assertEqual(AlgebraicCoordinate.from_string("azs543"), AlgebraicCoordinate(1370, 542))
