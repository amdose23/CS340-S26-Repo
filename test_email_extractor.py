import unittest
from email_extractor import extract_domain

class TestEmailExtractor(unittest.TestCase):
    def test_valid_email(self):
        self.assertEqual(extract_domain("user@example.com"), "example.com")

if __name__ == '__main__':
    unittest.main()