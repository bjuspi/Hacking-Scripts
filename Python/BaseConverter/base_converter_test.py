import unittest
from base_converter import base_to_decimal

class TestBaseToDecimal(unittest.TestCase):
    def test_binary_basic(self):
        testcase = "100011"
        base = 2
        expected = 35
        self.assertEqual(base_to_decimal(testcase, base), expected)

    def test_octal_basic(self):
        testcase = "176"
        base = 8
        expected = 126
        self.assertEqual(base_to_decimal(testcase, base), expected)

    def test_hexadecimal_basic(self):
        testcase = "7E"
        base = 16
        expected = 126
        self.assertEqual(base_to_decimal(testcase, base), expected)

    def test_zero(self):
        testcase = "0"
        base = 2
        expected = 0
        self.assertEqual(base_to_decimal(testcase, base), expected)

    def test_binary_fraction(self):
        testcase = "110.11"
        base = 2
        expected = 6.75
        self.assertEqual(base_to_decimal(testcase, base), expected)
        
    def test_octal_fraction(self):
        testcase = "23.17"
        base = 8
        expected = 19.234
        self.assertEqual(base_to_decimal(testcase, base), expected)
        
    def test_hexadecimal_fraction(self):
        testcase = "1A.23"
        base = 16
        expected = 26.137
        self.assertEqual(base_to_decimal(testcase, base), expected)

unittest.main()
    
