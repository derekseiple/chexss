"""
piece_color.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from src.utils.rgb_color import RgbColor


class PieceColor:
    """A PieceColor defines how the pieces will look on the board. They have a "main color" and and "accent color" which
    can be customized in the constructor, but generally one should use the static methods: White(), Silver(), and
    Black().
    """

    def __init__(
        self,
        main_color: RgbColor,
        accent_color: RgbColor
    ) -> None:
        self._main_color = main_color
        self._accent_color = accent_color

    @staticmethod
    def White() -> "PieceColor":
        return PieceColor(
            main_color=RgbColor(255, 255, 255),
            accent_color=RgbColor(192, 192, 192)
        )

    @staticmethod
    def Silver() -> "PieceColor":
        return PieceColor(
            main_color=RgbColor(192, 192, 192),
            accent_color=RgbColor(0, 0, 0)
        )

    @staticmethod
    def Black() -> "PieceColor":
        return PieceColor(
            main_color=RgbColor(0, 0, 0),
            accent_color=RgbColor(255, 255, 255)
        )

    @property
    def main_color(self) -> RgbColor:
        return self._main_color

    @property
    def accent_color(self) -> RgbColor:
        return self._accent_color
