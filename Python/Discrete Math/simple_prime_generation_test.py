# -*- coding: utf-8 -*-

import unittest
from simple_prime_generation import simple_prime_generation

class TestSimplePrimeGeneration(unittest.TestCase):
    def test_simple_prime_generation_basic(self):
        testcase = 5
        expected = [2, 3, 5]
        self.assertEqual(simple_prime_generation(testcase), expected)
        
    def test_is_prime_sqrt_basic_even(self):
        testcase = 10
        expected = [2, 3, 5, 7]
        self.assertEqual(simple_prime_generation(testcase), expected)
       
    def test_is_prime_sqrt_large(self):
        testcase = 30
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(simple_prime_generation(testcase), expected)
    
unittest.main()
