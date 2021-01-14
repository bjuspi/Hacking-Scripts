# -*- coding: utf-8 -*-

import unittest
from modular_factorial import modular_factorial

class TestModularFactorial(unittest.TestCase):
    def test_modular_factorial(self):
        # testcase
        n =  5
        k = 13
        
        # expected
        expected = 3
        self.assertEqual(modular_factorial(n, k), expected)

unittest.main()
