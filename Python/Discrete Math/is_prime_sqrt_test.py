# -*- coding: utf-8 -*-

import unittest
from is_prime_sqrt import is_prime_sqrt

class TestIsPrimeSqrt(unittest.TestCase):
    def test_is_prime_sqrt_basic(self):
        testcase = 5
        expected = True
        self.assertEqual(is_prime_sqrt(testcase), expected)
        
    def test_is_prime_sqrt_basic_even(self):
        testcase = 10
        expected = False
        self.assertEqual(is_prime_sqrt(testcase), expected)
       
    def test_is_prime_sqrt_large(self):
        testcase = 2887132691
        expected = True
        self.assertEqual(is_prime_sqrt(testcase), expected)
        
    def test_is_prime_sqrt_large_2(self):
        testcase = 2887132695
        expected = False
        self.assertEqual(is_prime_sqrt(testcase), expected)
    
unittest.main()
