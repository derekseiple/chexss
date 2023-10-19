"""
image_factory_utils.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from PIL import Image, ImageDraw, ImageFont
from src.board.board_coordinate import BoardCoordinate
from src.board.hex_meta import HexMeta
from src.board.board_coordinate_utils import get_algebraic_notation


def algebraic_coordinate_image_factory(
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
    (_, _, text_w, text_h) = draw.textbbox((0, 0), text, font=font)
    x = round((hex_meta.width - text_w) / 2)
    y = round((hex_meta.height - text_h) / 2)
    draw.text((x, y), text, fill=(0, 0, 0, 255), font=font)
    return img


def cube_coordinate_image_factory(
    dimension: int,
    coordinate: BoardCoordinate,
    hex_meta: HexMeta
) -> Image.Image:
    """Returns an image of the coordinate on the board using the cube coordinates.

    Parameters
    ----------
    coordinate: BoardCoordinate
        The coordinate on the board to draw the image at.

    hex_meta: HexMeta
        The metadata about the hexes.
    """
    img = Image.new("RGBA", (hex_meta.width, hex_meta.height), (255, 255, 255, 0))
    font = ImageFont.truetype("Arial Bold.ttf", int(0.2 * hex_meta.height))
    draw = ImageDraw.Draw(img)

    q_text = "{}".format(coordinate.q)
    r_text = "{}".format(coordinate.r)
    s_text = "{}".format(coordinate.s)
    if coordinate.q == 0 and coordinate.r == 0 and coordinate.s == 0:
        q_text = "q"
        r_text = "r"
        s_text = "s"

    qx = round(hex_meta.width / 4)
    qy = round(hex_meta.height / 8)
    draw.text((qx, qy), q_text, fill=(64, 128, 0, 255), font=font)

    (_, _, r_w, r_h) = draw.textbbox((0, 0), r_text, font=font)
    rx = round(15 * hex_meta.width / 16 - r_w)
    ry = round((hex_meta.height - r_h) / 2)
    draw.text((rx, ry), r_text, fill=(0, 119, 179, 255), font=font)

    sx = round(hex_meta.width / 4)
    sy = round(5 * hex_meta.height / 8)
    draw.text((sx, sy), s_text, fill=(184, 20, 184, 255), font=font)
    return img
