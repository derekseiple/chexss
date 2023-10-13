"""
rgb_color.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""


class RgbColor:
    """This class represents an RGB color."""

    def __init__(
        self,
        red: int,
        green: int,
        blue: int
    ) -> None:
        if red < 0 or red > 255:
            raise ValueError("Red value must be between 0 and 255.")
        if green < 0 or green > 255:
            raise ValueError("Green value must be between 0 and 255.")
        if blue < 0 or blue > 255:
            raise ValueError("Blue value must be between 0 and 255.")
        self._red: int = red
        self._green: int = green
        self._blue: int = blue

    def __str__(self) -> str:
        """Return the string representation of the color. This is useful for SVGs."""
        return 'rgb({0}, {1}, {2})'.format(self._red, self._green, self._blue)

    @property
    def rgb(self) -> tuple:
        """A tuple containing the red, green, and blue values."""
        return (self._red, self._green, self._blue)

    @property
    def red(self) -> int:
        """The red value of the color."""
        return self._red

    @property
    def green(self) -> int:
        """The green value of the color."""
        return self._green

    @property
    def blue(self) -> int:
        """The blue value of the color."""
        return self._blue
