# -*- coding: utf-8 -*-

import unittest
from is_prime_naive import is_prime_naive

class TestIsPrimeNaive(unittest.TestCase):
    def test_is_prime_naive_basic(self):
        testcase = 5
        expected = True
        self.assertEqual(is_prime_naive(testcase), expected)
    
    #def test_is_prime_naive_large(self):
    #    testcase = 2887132691
    #    expected = True
    #    self.assertEqual(is_prime_naive(testcase), expected)

unittest.main()
