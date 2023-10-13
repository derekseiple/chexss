"""
pawn.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from PIL import Image
from typing import Set
from src.board.board_state import BoardState
from src.board.board_coordinate import BoardCoordinate
from src.pieces.piece import Piece
from src.pieces.piece_color import PieceColor
from src.board.hex_meta import HexMeta
from src.pieces.pawn_image import PawnImage


class Pawn(Piece):
    """This class represents a pawn on the board. It is not a specific game piece that has a position on the board, but
    rather a general piece that that knows how the pawn can move and what it looks like.
    """

    def __init__(self) -> None:
        super().__init__()

    def image(
        self,
        meta: HexMeta,
        color: PieceColor
    ) -> Image:
        return PawnImage(meta, str(color.main_color), str(color.accent_color)).image

    def moves(
        self,
        coord: BoardCoordinate,
        board_sate: BoardState
    ) -> Set[BoardCoordinate]:
        pass
