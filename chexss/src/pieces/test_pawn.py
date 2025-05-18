"""
test_pawn.py
Copyright © 2025 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
import unittest
from src.pieces.piece_type import PieceType
from src.pieces.pawn import Pawn
from src.board.board import Board
from src.pieces.piece_utils import get_piece_from_type
from src.board.board_coordinate import BoardCoordinate
from src.board.board_state import BoardState, Player
from src.board.hex_meta import HexMeta
from src.pieces.piece_color import PieceColor


class TestPawn(unittest.TestCase):

    def test_can_draw_image(self):
        """We test that we can draw the image."""
        Pawn().image(HexMeta(50), PieceColor.White())

    def test_basic_moves(self):
        """We test the basic cases where there is a single pawn."""
        board: Board = Board(4)
        board_state: BoardState = (
            BoardState.builder(board)
            .add_piece(Player.WHITE, BoardCoordinate(0, 0), PieceType.PAWN)
            .add_piece(Player.WHITE, BoardCoordinate(1, -2), PieceType.PAWN)
            .add_piece(Player.BLACK, BoardCoordinate(-1, -1), PieceType.PAWN)
            .add_piece(Player.SILVER, BoardCoordinate(2, -1), PieceType.PAWN)
            .add_piece(Player.BLACK, BoardCoordinate(0, -1), PieceType.PAWN)
            .build())

        # Check the pawn at the origin
        coord = BoardCoordinate(0, 0)
        piece_info = board_state.get_piece_info(coord)
        self.assertEqual(piece_info.player, Player.WHITE)
        self.assertEqual(piece_info.piece_type, PieceType.PAWN)

        moves = get_piece_from_type(piece_info.piece_type).moves(coord, board_state)
        expected_moves = set([
            BoardCoordinate(-1, -1),
            BoardCoordinate(2, -1),
            BoardCoordinate(1, -1)])
        self.assertTrue(moves == expected_moves)

        # Check the pawn at the coordinate (2, -1)
        coord = BoardCoordinate(2, -1)
        piece_info = board_state.get_piece_info(coord)
        self.assertEqual(piece_info.player, Player.SILVER)
        self.assertEqual(piece_info.piece_type, PieceType.PAWN)

        moves = get_piece_from_type(piece_info.piece_type).moves(coord, board_state)
        expected_moves = set([
            BoardCoordinate(1, -1),
            BoardCoordinate(1, 0),
            BoardCoordinate(1, -2),
            BoardCoordinate(0, 0)])
        self.assertTrue(moves == expected_moves)

        # Check the pawn at the coordinate (0, -1)
        coord = BoardCoordinate(0, -1)
        piece_info = board_state.get_piece_info(coord)
        self.assertEqual(piece_info.player, Player.BLACK)
        self.assertEqual(piece_info.piece_type, PieceType.PAWN)

        moves = get_piece_from_type(piece_info.piece_type).moves(coord, board_state)
        expected_moves = set([
            BoardCoordinate(1, -1)])
        self.assertTrue(moves == expected_moves)
