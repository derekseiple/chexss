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
