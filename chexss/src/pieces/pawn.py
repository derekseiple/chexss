"""
pawn.py
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
from src.pieces.pawn_image import PawnImage
from src.pieces.piece_type import PieceType
from src.pieces.player import Player
from src.board.direction_iterator import DirectionDelta, DirectionIterator
from src.pieces.move_utils import is_valid_capture_location, location_is_occupied


class Pawn(Piece):
    """This class represents a pawn on the board. It is not a specific game piece that has a position on the board, but
    rather a general piece that knows how the pawn can move and what it looks like.
    """

    def __init__(self) -> None:
        super().__init__()

    def image(
        self,
        meta: HexMeta,
        color: PieceColor
    ) -> Image:
        return PawnImage(meta, str(color.main_color), str(color.accent_color)).image

    def moves(
        self,
        coord: BoardCoordinate,
        board_state: BoardState
    ) -> Set[BoardCoordinate]:
        """The pawn can move "forward" one space if those spaces are empty. It can capture diagonally forward one space
        if those spaces are occupied by an enemy piece.
        """
        player = Piece.get_player_and_validate_piece_type(coord, board_state, PieceType.PAWN)

        # the "forward" direction deltas depend on the player
        moves = set()
        move_directions = self.__move_direction_deltas(player)
        for direction in move_directions:
            it = DirectionIterator(coord, direction)
            for _ in range(1):
                next_coord = it.next()
                # The pawn can only move forward if the space is empty
                if (
                    board_state.board.is_valid_coordinate(next_coord) and
                    not location_is_occupied(next_coord, board_state)
                ):
                    moves.add(next_coord)
        # the "capture" direction deltas likewise depend on the player
        capture_directions = self.__capture_direction_deltas(player)
        for direction in capture_directions:
            it = DirectionIterator(coord, direction)
            for _ in range(1):
                next_coord = it.next()
                # The pawn can only capture if the space is occupied by an enemy piece
                if is_valid_capture_location(player, next_coord, board_state):
                    moves.add(next_coord)

        return moves

    def __move_direction_deltas(
        self,
        player: Player
    ) -> List[DirectionDelta]:
        if player == Player.WHITE:
            return [
                DirectionDelta(0, -1),
                DirectionDelta(1, -1)
            ]
        elif player == Player.SILVER:
            return [
                DirectionDelta(-1, 1),
                DirectionDelta(-1, 0)
            ]
        elif player == Player.BLACK:
            return [
                DirectionDelta(1, 0),
                DirectionDelta(0, 1)
            ]
        else:
            raise Exception("Invalid player.")

    def __capture_direction_deltas(
        self,
        player: Player
    ) -> List[DirectionDelta]:
        if player == Player.WHITE:
            return [
                DirectionDelta(-1, -1),
                DirectionDelta(1, -2),
                DirectionDelta(2, -1)
            ]
        elif player == Player.SILVER:
            return [
                DirectionDelta(-1, 2),
                DirectionDelta(-2, 1),
                DirectionDelta(-1, -1)
            ]
        elif player == Player.BLACK:
            return [
                DirectionDelta(2, -1),
                DirectionDelta(1, 1),
                DirectionDelta(-1, 2)
            ]
        else:
            raise Exception("Invalid player.")
