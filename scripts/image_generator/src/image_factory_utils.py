"""
image_factory_utils.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from PIL import Image, ImageDraw, ImageFont
from src.board_coordinates import BoardCoordinate
from src.hex_meta import HexMeta
from src.board_coordinate_utils import get_algebraic_notation


def coordinate_image_factory(
    dimension: int,
    coordinate: BoardCoordinate,
    hex_meta: HexMeta
) -> Image.Image:
    """Returns an image of the coordinate on the board using the algebraic notation.

    Parameters
    ----------
    coordinate: BoardCoordinate
        The coordinate on the board to draw the image at.
    
    hex_meta: HexMeta
        The metadata about the hexes.
    """
    img = Image.new("RGBA", (hex_meta.width, hex_meta.height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    text = get_algebraic_notation(dimension, coordinate)
    font = ImageFont.truetype("Arial Bold.ttf", int(hex_meta.height / 4))
    text_w, text_h = draw.textsize(text, font=font)
    x = round((hex_meta.width - text_w) / 2)
    y = round((hex_meta.height - text_h) / 2)
    draw.text((x, y), text, fill=(0, 0, 0, 255), font=font)
    return img
