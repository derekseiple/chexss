"""
math_utils.py
Copyright © 2023 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""


def RoundToEven(n) -> int:
    """Rounds the given number to the nearest even number."""
    return 2 * round(float(n) / 2.0)


def int_to_char_sequence(n: int) -> str:
    """Convert an integer to a character sequence (base 26) where:
    0 -> 'a'
    1 -> 'b'
    ...
    25 -> 'z'
    26 -> 'aa'
    27 -> 'ab'
    ...
    """
    if n < 0:
        raise ValueError("Input must be non-negative")

    result = ""
    while n >= 0:
        result = chr(ord('a') + (n % 26)) + result
        n = n // 26 - 1

    return result


def char_sequence_to_int(s: str) -> int:
    """Convert a character sequence back to an integer where:
    'a' -> 0
    'b' -> 1
    ...
    'z' -> 25
    'aa' -> 26
    'ab' -> 27
    etc.
    """
    if not all(c.isalpha() and c.islower() for c in s):
        raise ValueError("Input must be a non-empty string of lowercase letters")

    result = 0
    for i, char in enumerate(reversed(s)):
        result += (ord(char) - ord('a') + 1) * (26 ** i)
    return result - 1
