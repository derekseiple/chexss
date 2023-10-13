"""
math_utils.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""


def RoundToEven(n) -> int:
    """Rounds the given number to the nearest even number."""
    return 2 * round(float(n) / 2.0)
