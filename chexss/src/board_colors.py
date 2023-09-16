"""
board_colors.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from src.rgb_color import RgbColor


class BoardColors:
    """This class holds the colors for the board."""

    def __init__(
        self,
        white: RgbColor,
        silver: RgbColor,
        black: RgbColor,
    ) -> None:
        """Constructor.

        Parameters
        ----------
        white: RgbColor
            The color of the white hexes.
        
        silver: RgbColor
            The color of the silver hexes.

        black: RgbColor
            The color of the black hexes.
        """
        self._white = white
        self._silver = silver
        self._black = black

    @staticmethod
    def CreateDefault() -> "BoardColors":
        """Create the default board colors."""
        return BoardColors(
            white=RgbColor(255, 206, 158),
            silver=RgbColor(232, 171, 111),
            black=RgbColor(209, 139, 71)
        )

    @property
    def white(self) -> RgbColor:
        return self._white

    @property
    def silver(self) -> RgbColor:
        return self._silver
    
    @property
    def black(self) -> RgbColor:
        return self._black
