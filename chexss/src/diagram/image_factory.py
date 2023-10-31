"""
image_factory.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from abc import abstractmethod
from PIL import Image
from src.board.board_coordinate import BoardCoordinate
from src.board.hex_meta import HexMeta


class ImageFactory:
    """This class is an abstract base class that is used to create images for the board. Each subclass will implement
    the specifics for that type of image."""

    @abstractmethod
    def __call__(
        self,
        board_dimension: int,
        coordinate: BoardCoordinate,
        hex_meta: HexMeta
    ) -> Image.Image:
        """Return an image for the board, and size at the given coordinate."""
        raise NotImplementedError
