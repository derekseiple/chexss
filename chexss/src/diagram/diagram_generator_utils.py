"""
diagram_generator_utils.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from src.board.board_state import BoardState
from src.diagram.diagram_generator import DiagramGenerator
from src.board.board_image import BoardImage
from src.diagram.piece_image_factory import PieceImageFactory
from src.board.hex_meta import HexMeta
from src.pieces.piece_utils import get_piece_from_type
from src.board.board_coordinate import BoardCoordinate
from src.diagram.valid_move_image_factory import ValidMoveImageFactory


def get_diagram_generator_from_board_state(
    board_state: BoardState,
    hex_meta: HexMeta
) -> DiagramGenerator:
    """Returns a DiagramGenerator object from the given board state.

    Parameters
    ----------
    board_state: BoardState
        The board state to generate a diagram from.

    Returns
    -------
    DiagramGenerator
        The diagram generator object.
    """
    board_image = BoardImage(board_state.board, hex_meta)
    diagram_generator = DiagramGenerator(board_image)
    for coord, piece_info in board_state.piece_map.items():
        diagram_generator.draw(PieceImageFactory(piece_info), [coord])
    return diagram_generator


def get_diagram_generator_from_board_state_with_available_moves(
    board_state: BoardState,
    hex_meta: HexMeta,
    coord: BoardCoordinate,
) -> DiagramGenerator:
    """Returns a DiagramGenerator object from the given board along with all of the available moves for the piece at the
    given coordinate.

    Parameters
    ----------
    board_state: BoardState
        The board state to generate a diagram from.
    hex_meta: HexMeta
        The hex meta object to use for the diagram.
    coord: BoardCoordinate
        The coordinate of the piece to generate the moves diagram for.

    Returns
    -------
    DiagramGenerator
        The diagram generator object.
    """
    gen = get_diagram_generator_from_board_state(board_state, hex_meta)
    piece_info = board_state.get_piece_info(coord)
    if piece_info is None:
        raise Exception("There is no piece at coordinate {}.".format(coord))
    moves = get_piece_from_type(piece_info.piece_type).moves(coord, board_state)
    gen.draw(ValidMoveImageFactory(), list(moves))
    return gen
