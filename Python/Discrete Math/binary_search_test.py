# -*- coding: utf-8 -*-

import unittest
from binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_binary_search_basic_even(self):
        # testcase
        arr = [1, 2, 3, 5, 7, 10]
        n = 5
        
        # expected
        expected = 3
        self.assertEqual(binary_search(arr, n), expected)

    def test_binary_search_basic_odd(self):
        # testcase
        arr = [1, 2, 3, 5, 7, 10, 20]
        n = 10
        
        # expected
        expected = 5
        self.assertEqual(binary_search(arr, n), expected)

    def test_binary_search_not_found(self):
        # testcase
        arr = [1, 2, 3, 5, 7, 10]
        n = 4
        
        # expected
        expected = -1
        self.assertEqual(binary_search(arr, n), expected)

unittest.main()