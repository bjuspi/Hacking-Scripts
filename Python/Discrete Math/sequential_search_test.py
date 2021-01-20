# -*- coding: utf-8 -*-

import unittest
from sequential_search import sequential_search

class TestSequentialSearch(unittest.TestCase):
    def test_sequential_search_basic(self):
        # testcase
        arr = [1, 2, 3, 5, 7, 10]
        n = 5
        
        # expected
        expected = 3
        self.assertEqual(sequential_search(arr, n), expected)

    def test_sequential_search_not_found(self):
        # testcase
        arr = [1, 2, 3, 5, 7, 10]
        n = 4
        
        # expected
        expected = -1
        self.assertEqual(sequential_search(arr, n), expected)

unittest.main()
