"""
piece.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from abc import abstractmethod
from PIL import Image
from typing import List
from src.board_coordinates import BoardCoordinate
from src.pieces.piece_color import PieceColor
from src.hex_meta import HexMeta


class Piece:
    """This class represents a general piece on the board. This is an abstract base class. Each specific piece will
    inherit from this class and implement the specifics for that piece."""

    @abstractmethod
    def moves(
        self,
        coord: BoardCoordinate,
        dimension: int
    ) -> List[BoardCoordinate]:
        """Return the list of coordinates that this piece can move to from the given coordinate. This does not take
        into account the current state of the board, ie if the move would be blocked by another piece. This only
        returns the coordinates that the piece could move to if the board was empty.

        Parameters
        ----------
        coord: BoardCoordinate
            The coordinate location of the piece on the board.
        
        dimension: int
            The dimension of the board, ie the number of hexes on a side.
        
        ----------
        Returns: List[BoardCoordinate]
            The list of coordinates that this piece can move to from the given coordinate.
        """
        raise NotImplementedError


    @abstractmethod
    def image(
        self,
        meta: HexMeta,
        color: PieceColor
    ) -> Image:
        """Return the image of the piece scaled to fit on a hex of the given size."""
        raise NotImplementedError
