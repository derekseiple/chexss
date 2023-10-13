"""
piece_info.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from src.pieces.piece_type import PieceType
from src.pieces.player import Player


class PieceInfo:

    def __init__(
        self,
        player: Player,
        piece_type: PieceType
    ) -> None:
        self._player = player
        self._piece_type = piece_type

    @property
    def player(self) -> Player:
        return self._player

    @property
    def piece_type(self) -> PieceType:
        return self._piece_type
