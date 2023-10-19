"""
bishop.py
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
from src.pieces.bishop_image import BishopImage
from src.board.direction_utils import diagonal_direction_deltas
from src.board.direction_iterator import DirectionIterator
from src.pieces.piece_type import PieceType
from src.pieces.move_utils import is_valid_move_location, location_is_occupied
from src.pieces.player import Player


class Bishop(Piece):
    """This class represents a bishop on the board. It is not a specific game piece that has a position on the board, but
    rather a general piece that that knows how the bishop can move and what it looks like.
    """

    def __init__(self) -> None:
        super().__init__()

    def image(
        self,
        meta: HexMeta,
        color: PieceColor
    ) -> Image:
        return BishopImage(meta, str(color.main_color), str(color.accent_color)).image

    def moves(
        self,
        coord: BoardCoordinate,
        board_sate: BoardState
    ) -> Set[BoardCoordinate]:
        """The bishop can move in any diagonal direction as many spaces as it wants, but only if there are no pieces
        blocking the path and the space does not contain another piece of the same player."""
        # Check if the coordinate is on the board has a piece and get the color of the piece
        piece_info = board_sate.get_piece_info(coord)
        if piece_info is None:
            raise Exception("There is no piece at coordinate {}.".format(coord))
        # Make sure the piece is actually a king
        if piece_info.piece_type != PieceType.BISHOP:
            raise Exception("The piece at the coordinate {} is not a bishop.".format(coord))
        player: Player = piece_info.player

        # Loop through all of the directions and add the valid moves to the set
        moves = set()
        directions = diagonal_direction_deltas()
        for direction in directions:
            it = DirectionIterator(coord, direction)
            next_coord = it.next()
            while is_valid_move_location(player, next_coord, board_sate):
                # TODO: Make sure the move does not put the king in check.
                moves.add(next_coord)
                if location_is_occupied(next_coord, board_sate):
                    # If the location is occupied, we can't move past it so we break out of the loop
                    break
                next_coord = it.next()

        return moves
