import unittest
from Example_2 import *


class IsEvenFunc(unittest.TestCase):

    def test_is_even(self):
        self.assertEqual(is_even(2), 0)

    def test_is_even_nol(self):
        self.assertEqual(is_even(0), 0)

    def test_is_non_positive_even(self):
        self.assertEqual(is_even(-2), 0)

    def test_is_odd(self):
        self.assertEqual(is_even(3), 1)

    def test_is_non_positive_odd(self):
        self.assertEqual(is_even(-1), 1)


if __name__ == '__main__':
    unittest.main()
