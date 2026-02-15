import unittest
from list_max_finder import find_max

class TestListMaxFinder(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(find_max([1, 5, 2]), 5)

    def test_mixed_numbers(self):
        self.assertEqual(find_max([-10, 5, 2]), 5)

if __name__ == '__main__':
    unittest.main()