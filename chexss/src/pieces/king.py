"""
king.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from PIL import Image
from typing import Set
from src.board.board_coordinate import BoardCoordinate
from src.board.board_state import BoardState
from src.pieces.piece import Piece
from src.pieces.piece_color import PieceColor
from src.pieces.piece_type import PieceType
from src.board.hex_meta import HexMeta
from src.pieces.king_image import KingImage
from src.board.direction_utils import all_direction_deltas
from src.board.direction_iterator import DirectionIterator
from src.pieces.move_utils import is_valid_move_location


class King(Piece):
    """This class represents a king on the board. It is not a specific game piece that has a position on the board, but
    rather a general piece that that knows how the king can move and what it looks like.
    """

    def image(
        self,
        meta: HexMeta,
        color: PieceColor
    ) -> Image:
        return KingImage(meta, str(color.main_color), str(color.accent_color)).image

    def moves(
        self,
        coord: BoardCoordinate,
        board_state: BoardState
    ) -> Set[BoardCoordinate]:
        """The king can move in any direction, but only one space at a time and only if the space does not contain
        another piece of the same player."""
        player = Piece.get_player_and_validate_piece_type(coord, board_state, PieceType.KING)

        # Loop through all of the directions and add the valid moves to the set
        moves = set()
        directions = all_direction_deltas()
        for direction in directions:
            it = DirectionIterator(coord, direction)
            for _ in range(1):
                next_coord = it.next()
                if is_valid_move_location(player, next_coord, board_state):
                    moves.add(next_coord)

        return moves
