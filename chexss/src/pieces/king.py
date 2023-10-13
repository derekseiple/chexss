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

        # Note we could do this in a loop for this specific piece, but this starts the pattern of how we will do it for
        # other pieces. ie. we will have a set of directions and a loop for each direction until we hit a piece or the
        # edge of the board. We will probably refactor later as we develop other pieces.
        moves = set()

        # +q direction
        q_plus = BoardCoordinate(coord.q + 1, coord.r)
        if self.__is_valid_location(q_plus, board_sate, player):
            moves.add(q_plus)
        # -q direction
        q_minus = BoardCoordinate(coord.q - 1, coord.r)
        if self.__is_valid_location(q_minus, board_sate, player):
            moves.add(q_minus)
        # +r direction
        r_plus = BoardCoordinate(coord.q, coord.r + 1)
        if self.__is_valid_location(r_plus, board_sate, player):
            moves.add(r_plus)
        # -r direction
        r_minus = BoardCoordinate(coord.q, coord.r - 1)
        if self.__is_valid_location(r_minus, board_sate, player):
            moves.add(r_minus)
        # +s direction
        s_plus = BoardCoordinate(coord.q - 1, coord.r + 1)
        if self.__is_valid_location(s_plus, board_sate, player):
            moves.add(s_plus)
        # -s direction
        s_minus = BoardCoordinate(coord.q + 1, coord.r - 1)
        if self.__is_valid_location(s_minus, board_sate, player):
            moves.add(s_minus)

        # +q -r direction (q+1 r-2)
        q_plus_r_minus = BoardCoordinate(coord.q + 1, coord.r - 2)
        if self.__is_valid_location(q_plus_r_minus, board_sate, player):
            moves.add(q_plus_r_minus)
        # -q +r direction (q-1 r+2)
        q_minus_r_plus = BoardCoordinate(coord.q - 1, coord.r + 2)
        if self.__is_valid_location(q_minus_r_plus, board_sate, player):
            moves.add(q_minus_r_plus)
        # +r -s direction (q+1, r+1)
        r_plus_s_minus = BoardCoordinate(coord.q + 1, coord.r + 1)
        if self.__is_valid_location(r_plus_s_minus, board_sate, player):
            moves.add(r_plus_s_minus)
        # -r +s direction (q-1, r-1)
        r_minus_s_plus = BoardCoordinate(coord.q - 1, coord.r - 1)
        if self.__is_valid_location(r_minus_s_plus, board_sate, player):
            moves.add(r_minus_s_plus)
        # +q -s direction (q+2, r-1)
        q_plus_s_minus = BoardCoordinate(coord.q + 2, coord.r - 1)
        if self.__is_valid_location(q_plus_s_minus, board_sate, player):
            moves.add(q_plus_s_minus)
        # -q +s direction (q-2, r+1)
        q_minus_s_plus = BoardCoordinate(coord.q - 2, coord.r + 1)
        if self.__is_valid_location(q_minus_s_plus, board_sate, player):
            moves.add(q_minus_s_plus)

        return moves

    def __is_valid_location(self, coord: BoardCoordinate, board_sate: BoardState, player: Player) -> bool:
        """Make sure the coordinate is on the board and does not contain a piece of the same player."""
        # TODO: Make sure the coordinate is not in check
        # Make sure the coordinate is on the board
        if not board_sate.board.is_valid_coordinate(coord):
            return False
        # Make sure the coordinate does not contain a piece of the same player
        piece_info = board_sate.get_piece_info(coord)
        if piece_info is not None and piece_info.player == player:
            return False
        return True
