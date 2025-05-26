"""
piece.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from abc import abstractmethod
from PIL import Image
from typing import Set
from src.pieces.piece_type import PieceType
from src.pieces.player import Player
from src.pieces.piece_color import PieceColor
from src.board.hex_meta import HexMeta
from src.board.board_state import BoardState
from src.board.board_coordinate import BoardCoordinate


class Piece:
    """This class represents a general piece on the board. This is an abstract base class. Each specific piece will
    inherit from this class and implement the specifics for that piece."""

    @abstractmethod
    def image(
        self,
        meta: HexMeta,
        color: PieceColor
    ) -> Image:
        """Return the image of the piece scaled to fit on a hex of the given size."""
        raise NotImplementedError

    @abstractmethod
    def moves(
        self,
        coord: BoardCoordinate,
        board_sate: BoardState
    ) -> Set[BoardCoordinate]:
        """Return the set of coordinates that this piece can move to from the given coordinate. This will only return
        the set of coordinates that are valid based on the board state, but does not take into account the game rules
        like castling, putting your own king in check, etc. Those determinations will be made as part of the game state.

        Parameters
        ----------
        coord: BoardCoordinate
            The coordinate location of the piece on the board.

        board_sate: BoardState
            The state of the board. This is needed to determine if the move is blocked by another piece.

        ----------
        Returns: List[BoardCoordinate]
            The set of coordinates that this piece can move to from the given coordinate.
        """
        raise NotImplementedError

    @staticmethod
    def get_player_and_validate_piece_type(
        coord: BoardCoordinate,
        board_state: BoardState,
        piece_type: PieceType
    ) -> Player:
        """Validate that the piece at the given coordinate is of the correct type and get the player of that piece."""
        # Check if the coordinate is on the board has a piece and get the color of the piece
        piece_info = board_state.get_piece_info(coord)
        if piece_info is None:
            raise Exception("There is no piece at coordinate {}.".format(coord))
        # Make sure the piece is of the correct type
        if piece_info.piece_type != piece_type:
            raise Exception("The piece at the coordinate {} is not a {}.".format(coord, piece_type.name))
        return piece_info.player
