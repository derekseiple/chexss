"""
algebraic_coordinate_image_factory.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from PIL import Image
from src.board.board_coordinate import BoardCoordinate
from src.board.hex_meta import HexMeta
from src.diagram.image_factory import ImageFactory
from src.pieces.piece_info import PieceInfo
from src.pieces.piece_utils import get_piece_from_type, get_color_from_player


class PieceImageFactory(ImageFactory):
    """This class is used to create images for pieces on the board, based ont he given piece info."""

    def __init__(
        self,
        piece_info: PieceInfo
    ) -> None:
        self._piece_info = piece_info

    def __call__(
        self,
        board_dimension: int,
        coordinate: BoardCoordinate,
        hex_meta: HexMeta
    ) -> Image.Image:
        piece = get_piece_from_type(self._piece_info.piece_type)
        color = get_color_from_player(self._piece_info.player)
        return piece.image(hex_meta, color)
