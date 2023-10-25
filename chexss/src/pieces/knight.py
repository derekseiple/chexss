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
from src.pieces.player import Player
from src.board.direction_iterator import DirectionDelta
from src.board.direction_iterator import DirectionIterator
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
        board_sate: BoardState
    ) -> Set[BoardCoordinate]:
        """The knight can move in "L" shapes irregardless if any pieces are in the way."""
        # Check if the coordinate is on the board has a piece and get the color of the piece
        piece_info = board_sate.get_piece_info(coord)
        if piece_info is None:
            raise Exception("There is no piece at coordinate {}.".format(coord))
        # Make sure the piece is actually a knight
        if piece_info.piece_type != PieceType.KNIGHT:
            raise Exception("The piece at the coordinate {} is not a knight.".format(coord))
        player: Player = piece_info.player

        # Loop through all of the directions and add the valid moves to the set
        moves = set()
        directions = self.__knight_direction_deltas()
        for direction in directions:
            it = DirectionIterator(coord, direction)
            for _ in range(1):
                next_coord = it.next()
                if is_valid_move_location(player, next_coord, board_sate):
                    # TODO: Make sure the move does not put the king in check.
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
