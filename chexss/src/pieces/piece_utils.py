"""
piece_utils.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from src.pieces.piece import Piece
from src.pieces.piece_type import PieceType
from src.pieces.king import King
from src.pieces.queen import Queen
from src.pieces.rook import Rook
from src.pieces.bishop import Bishop
from src.pieces.knight import Knight
from src.pieces.pawn import Pawn


def get_piece_from_type(
    piece_type: PieceType
) -> Piece:
    """Returns a Piece object of the given type.

    Parameters
    ----------
    piece_type: PieceType
        The type of piece to return.
    """
    if piece_type == PieceType.KING:
        return King()
    elif piece_type == PieceType.QUEEN:
        return Queen()
    elif piece_type == PieceType.ROOK:
        return Rook()
    elif piece_type == PieceType.BISHOP:
        return Bishop()
    elif piece_type == PieceType.KNIGHT:
        return Knight()
    elif piece_type == PieceType.PAWN:
        return Pawn()
    else:
        raise ValueError("Unknown PieceType: {}".format(piece_type))
