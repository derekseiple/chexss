from math import sqrt
from PIL import Image, ImageDraw
from src.rbg_color import RbgColor


class HexImage:
    """This class wraps a Pillow image of a hex on the chexss board. On init, it will calculate the dimensions of the
    image and draw the hex according to the specified width and color. The image is drawn with a transparent background
    so they can be composed together to form the board.
    """

    def __init__(
        self,
        width: int,
        color: RbgColor
    ) -> None:
        """Constructor.

        Parameters
        ----------
        width: int
            The width of the kex in pixels. Must be an even number.

        color: RbgColor
            The color of the hex.
        """
        if width % 2 != 0:
            raise ValueError("Width must be an even number")
        
        # Set up the values we need to draw the hex
        self._color: RbgColor = color
        self._width: int = width
        self._height: int = round(2 * self._width / sqrt(3))
        vertical_step: int = round(self._width / sqrt(3) / 2)
        
        # Calculate the coordinates of the hex
        coords = [
            (int(self._width / 2), 0),
            (self._width - 1, vertical_step),
            (self._width - 1, self._height - 1 - vertical_step),
            (int(self._width / 2), self._height - 1),
            (int(self._width / 2) - 1, self._height - 1),
            (0, self._height - 1 - vertical_step),
            (0, vertical_step),
            (int(self._width / 2) - 1, 0)
        ]

        # Draw the hex
        self._image = Image.new("RGBA", (self._width, self._height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(self._image)
        draw.polygon(coords, fill=self._color.rgb, outline=self._color.rgb)


    @property
    def height(self) -> int:
        """The height of the hex in pixels."""
        return self._height
    
    @property
    def width(self) -> int:
        """The width of the hex in pixels."""
        return self._width
    
    @property
    def image(self) -> Image:
        """The Pillow image of the hex."""
        return self._image
