import unittest
from absolute_flipper import get_absolute_value

class TestAbsoluteFlipper(unittest.TestCase):
    def test_negative_input(self):
        self.assertEqual(get_absolute_value(-5), 5)

    def test_zero_input(self):
        self.assertEqual(get_absolute_value(0), 0)

if __name__ == '__main__':
    unittest.main()