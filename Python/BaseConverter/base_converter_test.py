import unittest
from base_converter import base_to_decimal

class TestDecimalToBase(unittest.TestCase):
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

unittest.main()
    
