"""
algebraic_coordinate_image_factory.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from PIL import Image, ImageDraw, ImageFont
from src.board.board_coordinate import BoardCoordinate
from src.board.hex_meta import HexMeta
from src.diagram.image_factory import ImageFactory
from src.board.board_coordinate_utils import get_algebraic_notation


class AlgebraicCoordinateImageFactory(ImageFactory):
    """This class is used to create images of the algebraic coordinates on the board."""

    def __call__(
        self,
        board_dimension: int,
        coordinate: BoardCoordinate,
        hex_meta: HexMeta
    ) -> Image.Image:
        img = Image.new("RGBA", (hex_meta.width, hex_meta.height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        text = get_algebraic_notation(board_dimension, coordinate)
        font = ImageFont.truetype("Arial Bold.ttf", int(hex_meta.height / 4))
        (_, _, text_w, text_h) = draw.textbbox((0, 0), text, font=font)
        x = round((hex_meta.width - text_w) / 2)
        y = round((hex_meta.height - text_h) / 2)
        draw.text((x, y), text, fill=(0, 0, 0, 255), font=font)
        return img
