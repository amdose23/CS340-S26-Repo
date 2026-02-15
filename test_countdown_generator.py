import unittest
from countdown_generator import generate_countdown

class TestCountdownGenerator(unittest.TestCase):
    def test_start_one(self):
        self.assertEqual(generate_countdown(1)[0], 1)

if __name__ == '__main__':
    unittest.main()