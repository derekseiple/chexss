"""
hex_meta.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from math import sqrt
from src.math_utils import RoundToEven


class HexMeta:
    """This class contains metadata about the hexes on the chexss board. It is used to calculate the coordinates of the
    hexagon that get used to draw the hex image. This class also contains the spacing and sizing information required to
    properly draw and layout multiple hexes.
    """

    def __init__(
        self,
        width: int
    ) -> None:
        """Constructor.

        Parameters
        ----------
        width: int
            The width of the hex in pixels. Must be an even number.
        """
        if width % 2 != 0:
            raise ValueError("Width must be an even number")

        self._width: int = width
        self._height: int = 2 * RoundToEven(self._width / sqrt(3))
        self._vertical_step: int = 3 * int(self._height / 4)
        self._horizontal_step: int = int(self._width / 2)
        coord_v_step: int = self._height / 4

        # Calculate the coordinates of the hex
        self._coords = [
            (self._horizontal_step, 0),
            (self._width - 1, coord_v_step),
            (self._width - 1, self._height - 1 - coord_v_step),
            (self._horizontal_step, self._height - 1),
            (self._horizontal_step - 1, self._height - 1),
            (0, self._height - 1 - coord_v_step),
            (0, coord_v_step),
            (self._horizontal_step - 1, 0)
        ]

    @property
    def height(self) -> int:
        """The height of the hex in pixels."""
        return self._height
    
    @property
    def width(self) -> int:
        """The width of the hex in pixels."""
        return self._width

    @property
    def vertical_step(self) -> int:
        """The vertical_step is the smallest distance so that the distance between the top of one hex and the top of
        another hex is a multiple of the vertical_step.
        """
        return self._vertical_step
    
    @property
    def horizontal_step(self) -> int:
        """The horizontal_step is the smallest distance so that the distance between the left side of one hex and the
        left side of another hex is a multiple of the horizontal_step."""
        return self._horizontal_step
    
    @property
    def coords(self) -> list:
        """The coordinates of the hex used to draw the image."""
        return self._coords
