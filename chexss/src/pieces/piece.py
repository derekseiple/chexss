"""
piece.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from abc import abstractmethod
from PIL import Image
from typing import Set
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
        """Return the set of coordinates that this piece can move to from the given coordinate.

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
