class RbgColor:
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
    
    @property
    def rgb(self) -> tuple:
        """A tuple containing the red, green, and blue values."""
        return (self._red, self._green, self._blue)

    @property
    def red(self) -> int:
        """TODO"""
        return self._red
    
    @property
    def green(self) -> int:
        """TODO"""
        return self._green
    
    @property
    def blue(self) -> int:
        """TODO"""
        return self._blue
