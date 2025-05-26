"""
knight.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from PIL import Image
from typing import Set, List
from src.board.board_state import BoardState
from src.board.board_coordinate import BoardCoordinate
from src.pieces.piece import Piece
from src.pieces.piece_color import PieceColor
from src.board.hex_meta import HexMeta
from src.pieces.knight_image import KnightImage
from src.pieces.piece_type import PieceType
from src.board.direction_iterator import DirectionDelta, DirectionIterator
from src.pieces.move_utils import is_valid_move_location


class Knight(Piece):
    """This class represents a knight on the board. It is not a specific game piece that has a position on the board, but
    rather a general piece that that knows how the knight can move and what it looks like.
    """

    def __init__(self) -> None:
        super().__init__()

    def image(
        self,
        meta: HexMeta,
        color: PieceColor
    ) -> Image:
        return KnightImage(meta, str(color.main_color), str(color.accent_color)).image

    def moves(
        self,
        coord: BoardCoordinate,
        board_state: BoardState
    ) -> Set[BoardCoordinate]:
        """The knight can move in "L" shapes irregardless if any pieces are in the way."""
        player = Piece.get_player_and_validate_piece_type(coord, board_state, PieceType.KNIGHT)

        # Loop through all of the directions and add the valid moves to the set
        moves = set()
        directions = self.__knight_direction_deltas()
        for direction in directions:
            it = DirectionIterator(coord, direction)
            for _ in range(1):
                next_coord = it.next()
                if is_valid_move_location(player, next_coord, board_state):
                    moves.add(next_coord)

        return moves

    def __knight_direction_deltas(self) -> List[DirectionDelta]:
        """Returns the direction deltas for the knight's moves."""
        return [
            DirectionDelta(1, -3),
            DirectionDelta(2, -3),
            DirectionDelta(3, -2),
            DirectionDelta(3, -1),
            DirectionDelta(2, 1),
            DirectionDelta(1, 2),
            DirectionDelta(-1, 3),
            DirectionDelta(-2, 3),
            DirectionDelta(-3, 2),
            DirectionDelta(-3, 1),
            DirectionDelta(-2, -1),
            DirectionDelta(-1, -2)
        ]
