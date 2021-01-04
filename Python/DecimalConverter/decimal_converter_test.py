import unittest
from decimal_converter import decimal_to_base

class TestDecimalToBase(unittest.TestCase):
    def test_binary_basic(self):
        testcase = 35
        base = 2
        expected = "100011"
        self.assertEqual(decimal_to_base(testcase, base), expected)
        
    def test_octal_basic(self):
        testcase = 126
        base = 8
        expected = "176"
        self.assertEqual(decimal_to_base(testcase, base), expected)
        
    def test_hexadecimal_basic(self):
        testcase = 126
        base = 16
        expected = "7E"
        self.assertEqual(decimal_to_base(testcase, base), expected)
    
    def test_zero(self):
        testcase = 0
        base = 2
        expected = "0"
        self.assertEqual(decimal_to_base(testcase, base), expected)
        
    def test_negative(self):
        pass

unittest.main()
