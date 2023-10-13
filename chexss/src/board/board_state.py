"""
board_state.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from typing import Dict, List, Optional
from src.board.board import Board
from src.board.board_coordinate import BoardCoordinate
from src.pieces.piece_type import PieceType
from src.pieces.player import Player
from src.pieces.piece_info import PieceInfo
import collections


class BoardStateBuilder:
    """This class is used to build a board state one piece at a time. It will ensure that the board state is valid, but
    it's main advantage is to provide a clear, clean interface for building a board state.
    """

    def __init__(
        self,
        board: Board
    ) -> None:
        self._board = board
        self._piece_map: Dict[BoardCoordinate, PieceInfo] = dict()
        self._player_piece_map: Dict[Player, List[BoardCoordinate]] = collections.defaultdict(list)

    def add_piece(
        self,
        player: Player,
        coord: BoardCoordinate,
        piece: PieceType
    ) -> 'BoardStateBuilder':
        if not self._board.is_valid_coordinate(coord):
            raise Exception("Coordinate {} is not a valid coordinate on the board.".format(coord))
        if coord in self._piece_map:
            raise Exception("There is already a piece at coordinate {}.".format(coord))

        self._piece_map[coord] = PieceInfo(player, piece)
        self._player_piece_map[player].append(coord)
        return self

    def build(self) -> 'BoardState':
        return BoardState(
            self._board,
            self._piece_map,
            self._player_piece_map
        )


class BoardState:
    """This class represents the state of the board at a given point in time. It contains all of the information about
    the board at that point in time. It is used to determine what moves are valid. Do not build this class directly,
    instead use the BoardStateBuilder class.
    """

    def __init__(
        self,
        board: Board,
        piece_map: Dict[BoardCoordinate, PieceInfo],
        player_piece_map: Dict[Player, List[BoardCoordinate]]
    ) -> None:
        """Use builder"""
        self._board = board
        self._piece_map: Dict[BoardCoordinate, PieceInfo] = piece_map
        self._player_piece_map: Dict[Player, List[BoardCoordinate]] = player_piece_map

    @staticmethod
    def builder(board: Board) -> BoardStateBuilder:
        return BoardStateBuilder(board)

    def get_piece_info(self, board_coordinate: BoardCoordinate) -> Optional[PieceInfo]:
        return self._piece_map.get(board_coordinate)

    @property
    def board(self) -> Board:
        return self._board
