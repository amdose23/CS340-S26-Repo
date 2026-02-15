import unittest
from grade_passer import is_passing

class TestGradePasser(unittest.TestCase):
    def test_high_score(self):
        self.assertTrue(is_passing(95))

    def test_failing_score(self):
        self.assertFalse(is_passing(40))

if __name__ == '__main__':
    unittest.main()