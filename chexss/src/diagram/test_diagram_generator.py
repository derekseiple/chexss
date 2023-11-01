"""
test_diagram_generator.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
import unittest
from src.board.board_coordinate import BoardCoordinate
from src.board.board_state import BoardState, BoardStateBuilder
from src.pieces.player import Player
from src.pieces.piece_type import PieceType
from src.board.board import Board
from src.board.hex_meta import HexMeta
from src.diagram.diagram_generator_utils import get_diagram_generator_from_board_state


class TestDiagramGenerator(unittest.TestCase):

    def test_can_generate_from_board_state(self):
        """We test that we can get a diagram generator from a board state. We don't test the validity of the generated
        image, just that we can generate it."""
        board_state: BoardState = (
            BoardStateBuilder(Board(7))
            .add_piece(Player.WHITE, BoardCoordinate(1, -4), PieceType.KING)
            .add_piece(Player.WHITE, BoardCoordinate(0, -4), PieceType.QUEEN)
            .add_piece(Player.SILVER, BoardCoordinate(0, -3), PieceType.KNIGHT)
            .add_piece(Player.BLACK, BoardCoordinate(2, -4), PieceType.KNIGHT)
            .build())

        get_diagram_generator_from_board_state(board_state, HexMeta(50))
