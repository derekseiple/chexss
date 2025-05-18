"""
board_state_utils.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from src.board.board_state import BoardState, BoardStateBuilder
from src.board.board import Board
from src.board.board_coordinate import BoardCoordinate
from src.pieces.piece_type import PieceType
from src.pieces.player import Player


def generate_initial_board_state() -> BoardState:
    """Generates the initial board state for a game of Chexss."""
    return (
        BoardStateBuilder(Board(7))
        # White pieces base row
        .add_piece(Player.WHITE, BoardCoordinate(-6, 6), PieceType.ROOK)
        .add_piece(Player.WHITE, BoardCoordinate(-5, 6), PieceType.KNIGHT)
        .add_piece(Player.WHITE, BoardCoordinate(-4, 6), PieceType.KING)
        .add_piece(Player.WHITE, BoardCoordinate(-3, 6), PieceType.BISHOP)
        .add_piece(Player.WHITE, BoardCoordinate(-2, 6), PieceType.QUEEN)
        .add_piece(Player.WHITE, BoardCoordinate(-1, 6), PieceType.KNIGHT)
        .add_piece(Player.WHITE, BoardCoordinate(0, 6), PieceType.ROOK)
        # White pieces second row
        .add_piece(Player.WHITE, BoardCoordinate(-6, 5), PieceType.PAWN)
        .add_piece(Player.WHITE, BoardCoordinate(-5, 5), PieceType.PAWN)
        .add_piece(Player.WHITE, BoardCoordinate(-4, 5), PieceType.PAWN)
        .add_piece(Player.WHITE, BoardCoordinate(-3, 5), PieceType.BISHOP)
        .add_piece(Player.WHITE, BoardCoordinate(-2, 5), PieceType.BISHOP)
        .add_piece(Player.WHITE, BoardCoordinate(-1, 5), PieceType.PAWN)
        .add_piece(Player.WHITE, BoardCoordinate(0, 5), PieceType.PAWN)
        .add_piece(Player.WHITE, BoardCoordinate(1, 5), PieceType.PAWN)
        # White pieces third row
        .add_piece(Player.WHITE, BoardCoordinate(-5, 4), PieceType.PAWN)
        .add_piece(Player.WHITE, BoardCoordinate(-4, 4), PieceType.PAWN)
        .add_piece(Player.WHITE, BoardCoordinate(-3, 4), PieceType.PAWN)
        .add_piece(Player.WHITE, BoardCoordinate(-2, 4), PieceType.PAWN)
        .add_piece(Player.WHITE, BoardCoordinate(-1, 4), PieceType.PAWN)
        .add_piece(Player.WHITE, BoardCoordinate(0, 4), PieceType.PAWN)
        .add_piece(Player.WHITE, BoardCoordinate(1, 4), PieceType.PAWN)
        # White pieces fourth row
        .add_piece(Player.WHITE, BoardCoordinate(-2, 3), PieceType.PAWN)
        .add_piece(Player.WHITE, BoardCoordinate(-1, 3), PieceType.PAWN)
        # Silver pieces base row
        .add_piece(Player.SILVER, BoardCoordinate(6, 0), PieceType.ROOK)
        .add_piece(Player.SILVER, BoardCoordinate(6, -1), PieceType.KNIGHT)
        .add_piece(Player.SILVER, BoardCoordinate(6, -2), PieceType.KING)
        .add_piece(Player.SILVER, BoardCoordinate(6, -3), PieceType.BISHOP)
        .add_piece(Player.SILVER, BoardCoordinate(6, -4), PieceType.QUEEN)
        .add_piece(Player.SILVER, BoardCoordinate(6, -5), PieceType.KNIGHT)
        .add_piece(Player.SILVER, BoardCoordinate(6, -6), PieceType.ROOK)
        # Silver pieces second row
        .add_piece(Player.SILVER, BoardCoordinate(5, 1), PieceType.PAWN)
        .add_piece(Player.SILVER, BoardCoordinate(5, 0), PieceType.PAWN)
        .add_piece(Player.SILVER, BoardCoordinate(5, -1), PieceType.PAWN)
        .add_piece(Player.SILVER, BoardCoordinate(5, -2), PieceType.BISHOP)
        .add_piece(Player.SILVER, BoardCoordinate(5, -3), PieceType.BISHOP)
        .add_piece(Player.SILVER, BoardCoordinate(5, -4), PieceType.PAWN)
        .add_piece(Player.SILVER, BoardCoordinate(5, -5), PieceType.PAWN)
        .add_piece(Player.SILVER, BoardCoordinate(5, -6), PieceType.PAWN)
        # Silver pieces third row
        .add_piece(Player.SILVER, BoardCoordinate(4, 1), PieceType.PAWN)
        .add_piece(Player.SILVER, BoardCoordinate(4, 0), PieceType.PAWN)
        .add_piece(Player.SILVER, BoardCoordinate(4, -1), PieceType.PAWN)
        .add_piece(Player.SILVER, BoardCoordinate(4, -2), PieceType.PAWN)
        .add_piece(Player.SILVER, BoardCoordinate(4, -3), PieceType.PAWN)
        .add_piece(Player.SILVER, BoardCoordinate(4, -4), PieceType.PAWN)
        .add_piece(Player.SILVER, BoardCoordinate(4, -5), PieceType.PAWN)
        # Silver pieces fourth row
        .add_piece(Player.SILVER, BoardCoordinate(3, -1), PieceType.PAWN)
        .add_piece(Player.SILVER, BoardCoordinate(3, -2), PieceType.PAWN)
        # Black pieces base row
        .add_piece(Player.BLACK, BoardCoordinate(0, -6), PieceType.ROOK)
        .add_piece(Player.BLACK, BoardCoordinate(-1, -5), PieceType.KNIGHT)
        .add_piece(Player.BLACK, BoardCoordinate(-2, -4), PieceType.KING)
        .add_piece(Player.BLACK, BoardCoordinate(-3, -3), PieceType.BISHOP)
        .add_piece(Player.BLACK, BoardCoordinate(-4, -2), PieceType.QUEEN)
        .add_piece(Player.BLACK, BoardCoordinate(-5, -1), PieceType.KNIGHT)
        .add_piece(Player.BLACK, BoardCoordinate(-6, 0), PieceType.ROOK)
        # Black pieces second row
        .add_piece(Player.BLACK, BoardCoordinate(1, -6), PieceType.PAWN)
        .add_piece(Player.BLACK, BoardCoordinate(0, -5), PieceType.PAWN)
        .add_piece(Player.BLACK, BoardCoordinate(-1, -4), PieceType.PAWN)
        .add_piece(Player.BLACK, BoardCoordinate(-2, -3), PieceType.BISHOP)
        .add_piece(Player.BLACK, BoardCoordinate(-3, -2), PieceType.BISHOP)
        .add_piece(Player.BLACK, BoardCoordinate(-4, -1), PieceType.PAWN)
        .add_piece(Player.BLACK, BoardCoordinate(-5, 0), PieceType.PAWN)
        .add_piece(Player.BLACK, BoardCoordinate(-6, 1), PieceType.PAWN)
        # Black pieces third row
        .add_piece(Player.BLACK, BoardCoordinate(1, -5), PieceType.PAWN)
        .add_piece(Player.BLACK, BoardCoordinate(0, -4), PieceType.PAWN)
        .add_piece(Player.BLACK, BoardCoordinate(-1, -3), PieceType.PAWN)
        .add_piece(Player.BLACK, BoardCoordinate(-2, -2), PieceType.PAWN)
        .add_piece(Player.BLACK, BoardCoordinate(-3, -1), PieceType.PAWN)
        .add_piece(Player.BLACK, BoardCoordinate(-4, 0), PieceType.PAWN)
        .add_piece(Player.BLACK, BoardCoordinate(-5, 1), PieceType.PAWN)
        # Black pieces fourth row
        .add_piece(Player.BLACK, BoardCoordinate(-1, -2), PieceType.PAWN)
        .add_piece(Player.BLACK, BoardCoordinate(-2, -1), PieceType.PAWN)
        .build())
