"""
test_math_utils.py
Copyright © 2025 Derek Seiple
Licensed under Creative Commons BY-NC-SA 3.0. See license file.
"""
import unittest
from src.utils.math_utils import int_to_char_sequence, char_sequence_to_int


class TestMathUtils(unittest.TestCase):

    def test_int_to_char_sequence(self):
        """We test that we can convert an integer to a character sequence."""
        self.assertEqual(int_to_char_sequence(0), 'a')
        self.assertEqual(int_to_char_sequence(1), 'b')
        self.assertEqual(int_to_char_sequence(25), 'z')
        self.assertEqual(int_to_char_sequence(26), 'aa')
        self.assertEqual(int_to_char_sequence(27), 'ab')
        self.assertEqual(int_to_char_sequence(28), 'ac')
        self.assertEqual(int_to_char_sequence(52), 'ba')
        self.assertEqual(int_to_char_sequence(53), 'bb')
        self.assertEqual(int_to_char_sequence(54), 'bc')
        self.assertEqual(int_to_char_sequence(701), 'zz')
        self.assertEqual(int_to_char_sequence(702), 'aaa')
        self.assertEqual(int_to_char_sequence(703), 'aab')
        self.assertEqual(int_to_char_sequence(704), 'aac')

    def test_char_sequence_to_int(self):
        """We test that we can convert a character sequence to an integer."""
        self.assertEqual(char_sequence_to_int('a'), 0)
        self.assertEqual(char_sequence_to_int('b'), 1)
        self.assertEqual(char_sequence_to_int('z'), 25)
        self.assertEqual(char_sequence_to_int('aa'), 26)
        self.assertEqual(char_sequence_to_int('ab'), 27)
        self.assertEqual(char_sequence_to_int('ac'), 28)
        self.assertEqual(char_sequence_to_int('ba'), 52)
        self.assertEqual(char_sequence_to_int('bb'), 53)
        self.assertEqual(char_sequence_to_int('bc'), 54)
        self.assertEqual(char_sequence_to_int('zz'), 701)
        self.assertEqual(char_sequence_to_int('aaa'), 702)
        self.assertEqual(char_sequence_to_int('aab'), 703)
        self.assertEqual(char_sequence_to_int('aac'), 704)
