"""
capturing_move_image_factory.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from PIL import Image, ImageDraw
from src.board.board_coordinate import BoardCoordinate
from src.board.hex_meta import HexMeta
from src.diagram.image_factory import ImageFactory


class CapturingMoveImageFactory(ImageFactory):
    """This class is used to create images for pieces on the board, based ont he given piece info."""

    def __call__(
        self,
        board_dimension: int,
        coordinate: BoardCoordinate,
        hex_meta: HexMeta
    ) -> Image.Image:
        img = Image.new("RGBA", (hex_meta.width, hex_meta.height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        # define a square 1/4 the size of the hex width
        square_size = round(hex_meta.width / 4)
        # define the top left corner of the square
        x = round((hex_meta.width - square_size) / 2)
        y = round((hex_meta.height - square_size) / 2)
        # define the bottom right corner of the square
        x1 = x + square_size
        y1 = y + square_size
        draw.line([(x, y), (x1, y1)], fill="red", width=round(square_size/4))
        draw.line([(x1, y), (x, y1)], fill="red", width=round(square_size/4))

        return img
