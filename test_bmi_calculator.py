import unittest
from bmi_calculator import calculate_bmi

class TestBMICalculator(unittest.TestCase):
    def test_unit_dimensions(self):
        self.assertEqual(calculate_bmi(1, 1), 1)

if __name__ == '__main__':
    unittest.main()