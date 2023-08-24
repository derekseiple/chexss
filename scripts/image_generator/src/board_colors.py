"""
board_colors.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
from src.rbg_color import RbgColor


class BoardColors:
    """This class holds the colors for the board."""

    def __init__(
        self,
        white: RbgColor,
        silver: RbgColor,
        black: RbgColor,
    ) -> None:
        """Constructor.

        Parameters
        ----------
        white: RbgColor
            The color of the white hexes.
        
        silver: RbgColor
            The color of the silver hexes.

        black: RbgColor
            The color of the black hexes.
        """
        self._white = white
        self._silver = silver
        self._black = black

    @staticmethod
    def CreateDefault() -> "BoardColors":
        """Create the default board colors."""
        return BoardColors(
            white=RbgColor(255, 206, 158),
            silver=RbgColor(232, 171, 111),
            black=RbgColor(209, 139, 71)
        )

    @property
    def white(self) -> RbgColor:
        return self._white

    @property
    def silver(self) -> RbgColor:
        return self._silver
    
    @property
    def black(self) -> RbgColor:
        return self._black
