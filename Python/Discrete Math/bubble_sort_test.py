import unittest
from bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort_basic(self):
        testcase = [5, 1, 7, 10, 3, 3, 6, 8, 2]
        expected = [1, 2, 3, 3, 5, 6, 7, 8, 10]
        self.assertEqual(bubble_sort(testcase), expected)

    def test_bubble_sort_large(self):
        testcase = [1, 100, 5, 20, 1000, 500, 2000, 3]
        expected = [1, 3, 5, 20, 100, 500, 1000, 2000]
        self.assertEqual(bubble_sort(testcase), expected)

unittest.main()