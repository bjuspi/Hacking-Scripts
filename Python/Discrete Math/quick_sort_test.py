import unittest
from quick_sort import quick_sort

class TestQuickSort(unittest.TestCase):
    def test_quick_sort_basic(self):
        testcase = [5, 1, 7, 10, 3, 3, 6, 8, 2]
        expected = [1, 2, 3, 3, 5, 6, 7, 8, 10]
        self.assertEqual(quick_sort(testcase, 0, len(testcase)-1), expected)

    def test_quick_sort_large(self):
        testcase = [1, 100, 5, 20, 1000, 500, 2000, 3]
        expected = [1, 3, 5, 20, 100, 500, 1000, 2000]
        self.assertEqual(quick_sort(testcase, 0, len(testcase)-1), expected)

unittest.main()