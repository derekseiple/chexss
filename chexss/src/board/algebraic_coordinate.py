"""
algebraic_coordinate.py
Copyright © 2025 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from src.utils.math_utils import int_to_char_sequence, char_sequence_to_int


class AlgebraicCoordinate:
    """This class represents a coordinate on the board in algebraic notation. The algebraic notation is a string that
    starts with one or more letters, followed by one or more numbers. The letters represent the column, and the numbers
    represent the row. Not all letter/number combinations represent valid board coordinates. But determining if it is
    valid depends on the dimension of the board. So we don't validate the algebraic notation here. The
    CoordinateConverter class will handle any validation that is needed.
    """

    def __init__(self, column: int, row: int) -> None:
        """Constructor.

        Parameters
        ----------
        column : int
            The column of the coordinate. A value of 0 represents the leftmost column and is represented by the letter
            'a'. Increasing values of column represent increasing letters which wrap around to `aa`, `ab`, etc.
        row : int
            The row of the coordinate. A value of 0 represents the bottommost row and is represented by the number 1.
            Increasing values of row represent increasing numbers.
        """
        self._column = column
        self._row = row

    @property
    def column(self) -> int:
        """The column of the coordinate."""
        return self._column

    @property
    def column_string(self) -> str:
        """The column of the coordinate as a string."""
        return int_to_char_sequence(self.column)

    @property
    def row(self) -> int:
        """The row of the coordinate as a string."""
        return self._row

    @property
    def row_string(self) -> str:
        """The row of the coordinate as a string."""
        return str(self.row + 1)

    def __str__(self) -> str:
        return f"{self.column_string}{self.row_string}"

    def __repr__(self) -> str:
        return f"AlgebraicCoordinate(column={self.column}, row={self.row})"

    def __eq__(self, other: object) -> bool:
        """Check if two AlgebraicCoordinates are equal."""
        if not isinstance(other, AlgebraicCoordinate):
            return False
        return self.column == other.column and self.row == other.row

    @staticmethod
    def from_string(notation: str) -> 'AlgebraicCoordinate':
        """Create an AlgebraicCoordinate from a string."""
        for i, char in enumerate(notation):
            if not char.isalpha():
                column_string = notation[:i]
                row_string = notation[i:]
                break
        return AlgebraicCoordinate(char_sequence_to_int(column_string), int(row_string) - 1)
