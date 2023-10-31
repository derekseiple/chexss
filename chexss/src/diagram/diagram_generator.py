"""
diagram_generator.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from PIL import Image
from typing import List
from src.diagram.image_factory import ImageFactory
from src.board.board_image import BoardImage
from src.board.board_coordinate import BoardCoordinate
from src.board.board_coordinate_utils import board_coordinate_image_location


class DiagramGenerator:
    """This class is constructed with a BoardImage which is then used as a base to draw other images on top of it. The
    draw method below will then draw images on top of the board image at the given coordinates.
    """

    def __init__(
        self,
        board_image: BoardImage,
    ) -> None:
        self._board_image = board_image
        self._image = self._board_image.image.copy()

    def draw(
        self,
        image_factory: ImageFactory,
        coordinates: List[BoardCoordinate]
    ) -> None:
        """For each coordinate in the list, draw the image returned by the image factory at the coordinate on the board.

        Parameters
        ----------
        image_factory: ImageFactory
            The image factory to use to create the images to draw on the board.

        coordinates: List[BoardCoordinate]
            The coordinates on the board to draw the images at with the image factory.
        """
        for coordinate in coordinates:
            self._image.alpha_composite(
                image_factory(self._board_image.dimension, coordinate, self._board_image.hex_meta),
                board_coordinate_image_location(self._board_image.dimension, coordinate, self._board_image.hex_meta)
            )

    @property
    def image(self) -> Image.Image:
        return self._image
