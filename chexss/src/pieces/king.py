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
from src.pieces.player import Player
from src.board.direction_utils import all_direction_deltas
from src.board.direction_iterator import DirectionIterator


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
        board_sate: BoardState
    ) -> Set[BoardCoordinate]:
        """The king can move in any direction, but only one space at a time and only if the space does not contain
        another piece of the same player."""
        # Check if the coordinate is on the board has a piece and get the color of the piece
        piece_info = board_sate.get_piece_info(coord)
        if piece_info is None:
            raise Exception("There is no piece at coordinate {}.".format(coord))
        # Make sure the piece is actually a king
        if piece_info.piece_type != PieceType.KING:
            raise Exception("The piece at the coordinate {} is not a king.".format(coord))
        player = piece_info.player

        # Loop through all of the directions and add the valid moves to the set
        moves = set()
        directions = all_direction_deltas()
        for direction in directions:
            it = DirectionIterator(coord, direction)
            for _ in range(1):
                next_coord = it.next()
                if self.__is_valid_location(next_coord, board_sate, player):
                    moves.add(next_coord)

        return moves

    def __is_valid_location(self, coord: BoardCoordinate, board_sate: BoardState, player: Player) -> bool:
        """Make sure the coordinate is on the board and does not contain a piece of the same player."""
        # TODO: Make sure the coordinate is not in check. We can come up with a method to see what pieces are attacking
        # a particular coordinate once we have the logic of how each piece can move.

        # Make sure the coordinate is on the board
        if not board_sate.board.is_valid_coordinate(coord):
            return False

        # Make sure the coordinate does not contain a piece of the same player
        piece_info = board_sate.get_piece_info(coord)
        if piece_info is not None and piece_info.player == player:
            return False
        return True
