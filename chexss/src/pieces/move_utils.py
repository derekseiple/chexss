"""
move_utils.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from src.pieces.player import Player
from src.board.board_coordinate import BoardCoordinate
from src.board.board_state import BoardState


def is_valid_move_location(player: Player, coord: BoardCoordinate, board_sate: BoardState) -> bool:
    """This is a utility function that checks if the given coordinate is a valid location for a move for a particular
    player. This does not check anything specific to the piece like if that particular piece could have moved to that
    location (the individual piece classes will do that), or that the move results in a valid position (ie own king not
    put in check), just that the coordinate is on the board and that the coordinate does not contain a piece of the
    same player."""

    # Make sure the coordinate is on the board
    if not board_sate.board.is_valid_coordinate(coord):
        return False

    # Make sure the coordinate does not contain a piece of the same player
    piece_info = board_sate.get_piece_info(coord)
    if piece_info is not None and piece_info.player == player:
        return False
    return True


def is_valid_capture_location(player: Player, coord: BoardCoordinate, board_sate: BoardState) -> bool:
    """This is a utility function that is similar to is_valid_move_location. The difference here is that this function
    will return True if the coordinate contains a piece of the opposite player, but False if the coordinate is empty or
    contains a piece of the same player."""

    # Make sure the coordinate is on the board
    if not board_sate.board.is_valid_coordinate(coord):
        return False

    # Make sure the coordinate contains an enemy piece
    piece_info = board_sate.get_piece_info(coord)
    if piece_info is not None and piece_info.player != player:
        return True
    return False


def location_is_occupied(coord: BoardCoordinate, board_sate: BoardState) -> bool:
    """This is a utility function that checks if the given coordinate is occupied by a piece."""
    piece_info = board_sate.get_piece_info(coord)
    return piece_info is not None
