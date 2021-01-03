# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 20:26:52 2021

@author: bjusp
"""
from decimal_converter import decimal_to_base
import unittest

class TestDecimalToBase(unittest.TestCase):
    def test_binary_basic(self):
        testcase = 35
        base = 2
        expected = 100011
        self.assertEqual(decimal_to_base(testcase, base), expected)
        
    def test_octal_basic(self):
        testcase = 126
        base = 8
        expected = 176
        self.assertEqual(decimal_to_base(testcase, base), expected)
        
    def test_zero(self):
        testcase = 0
        base = 2
        expected = 0
        self.assertEqual(decimal_to_base(testcase, base), expected)
        
    def test_negative(self):
        pass

unittest.main()