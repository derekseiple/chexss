"""
test_rook.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
import unittest
from src.pieces.piece_type import PieceType
from src.pieces.rook import Rook
from src.board.board import Board
from src.pieces.piece_utils import get_piece_from_type
from src.board.board_coordinate import BoardCoordinate
from src.board.board_state import BoardState, BoardStateBuilder, Player
from src.board.hex_meta import HexMeta
from src.pieces.piece_color import PieceColor


class TestRook(unittest.TestCase):

    def test_can_draw_image(self):
        """We test that we can draw the image."""
        Rook().image(HexMeta(50), PieceColor.White())

    def test_basic_moves(self):
        """We test the basic case where there are no other pieces on the board except a single rook."""
        board: Board = Board(4)
        rook_coord: BoardCoordinate = BoardCoordinate(3, -3)
        board_state: BoardState = (
            BoardState.builder(board)
            .add_piece(Player.WHITE, rook_coord, PieceType.ROOK)
            .build())

        # We want to test we can get the appropriate Moves class so we get that from the piece on the board itself.
        piece_info = board_state.get_piece_info(rook_coord)
        self.assertEqual(piece_info.player, Player.WHITE)
        self.assertEqual(piece_info.piece_type, PieceType.ROOK)

        moves = get_piece_from_type(piece_info.piece_type).moves(rook_coord, board_state)
        expected_moves = set((
            BoardCoordinate(0, -3),
            BoardCoordinate(1, -3),
            BoardCoordinate(2, -3),
            BoardCoordinate(-3, 3),
            BoardCoordinate(-2, 2),
            BoardCoordinate(-1, 1),
            BoardCoordinate(0, 0),
            BoardCoordinate(1, -1),
            BoardCoordinate(2, -2),
            BoardCoordinate(3, 0),
            BoardCoordinate(3, -1),
            BoardCoordinate(3, -2)))

        self.assertTrue(moves == expected_moves)

    def test_moves_with_other_pieces(self):
        """We test that it moves properly when there are other pieces on the board."""
        board: Board = Board(4)
        rook_coord: BoardCoordinate = BoardCoordinate(3, -3)
        board_state: BoardState = (
            BoardStateBuilder(board)
            .add_piece(Player.WHITE, rook_coord, PieceType.ROOK)
            .add_piece(Player.WHITE, BoardCoordinate(3, -1), PieceType.KING)
            .add_piece(Player.SILVER, BoardCoordinate(2, -1), PieceType.KNIGHT)
            .add_piece(Player.SILVER, BoardCoordinate(1, -3), PieceType.KNIGHT)
            .add_piece(Player.BLACK, BoardCoordinate(-1, 1), PieceType.KNIGHT)
            .build())

        # We want to test we can get the appropriate Moves class so we get that from the piece on the board itself.
        piece_info = board_state.get_piece_info(rook_coord)
        self.assertEqual(piece_info.player, Player.WHITE)
        self.assertEqual(piece_info.piece_type, PieceType.ROOK)

        moves = get_piece_from_type(piece_info.piece_type).moves(rook_coord, board_state)
        expected_moves = set((
            BoardCoordinate(1, -3),
            BoardCoordinate(2, -3),
            BoardCoordinate(-1, 1),
            BoardCoordinate(0, 0),
            BoardCoordinate(1, -1),
            BoardCoordinate(2, -2),
            BoardCoordinate(3, -2)))

        self.assertTrue(moves == expected_moves)

    def test_moving_piece_that_doesnt_exist_fails(self):
        """If we try to get moves for a coordinate that does not have a piece we should fail."""
        board: Board = Board(7)
        rook_coord: BoardCoordinate = BoardCoordinate(1, -4)
        board_state: BoardState = (
            BoardStateBuilder(board)
            .add_piece(Player.WHITE, rook_coord, PieceType.ROOK)
            .build())

        with self.assertRaises(Exception):
            Rook().moves(BoardCoordinate(0, 0), board_state)

    def test_moving_non_rook_fails(self):
        """If we try to get moves for a coordinate that is not a rook we should fail."""
        board: Board = Board(7)
        king_coord: BoardCoordinate = BoardCoordinate(1, -4)
        rook_coord: BoardCoordinate = BoardCoordinate(0, -4)
        board_state: BoardState = (
            BoardStateBuilder(board)
            .add_piece(Player.WHITE, king_coord, PieceType.KING)
            .add_piece(Player.WHITE, rook_coord, PieceType.ROOK)
            .build())

        piece_info = board_state.get_piece_info(rook_coord)
        with self.assertRaises(Exception):
            get_piece_from_type(piece_info.piece_type).moves(king_coord, board_state)
