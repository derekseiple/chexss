"""
valid_move_image_factory.py
Copyright © 2025 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from PIL import Image, ImageDraw
from src.board.board_coordinate import BoardCoordinate
from src.board.hex_meta import HexMeta
from src.diagram.image_factory import ImageFactory


class ValidMoveImageFactory(ImageFactory):
    """This class is used to create a circle image that can be used to indicate a valid move, which can be layered on
    top of an existing diagram.
    """

    def __call__(
        self,
        board_dimension: int,
        coordinate: BoardCoordinate,
        hex_meta: HexMeta
    ) -> Image.Image:
        img = Image.new("RGBA", (hex_meta.width, hex_meta.height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        # define a circle 1/8 the size of the hex width
        circle_size = round(hex_meta.width / 8)
        # Bounding box of the circle
        left = (hex_meta.width - circle_size) / 2
        top = (hex_meta.height - circle_size) / 2
        right = left + circle_size
        bottom = top + circle_size
        # Draw the circle
        draw.ellipse([(left, top), (right, bottom)], fill="red", width=round(circle_size / 4))
        return img
