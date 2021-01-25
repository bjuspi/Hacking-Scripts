import unittest
from subset_sum import subset_sum

class TestSubsetSum(unittest.TestCase):
    def test_subset_sum_basic(self):
        testcase = [5, 1, 7, 10, 3, 3, 6, 8, 2]
        k = 11
        expected = True
        self.assertEqual(subset_sum(testcase, k), expected)

    def test_subset_sum_large(self):
        testcase = [100, 200, 300, 400, 500]
        k = 2000
        expected = False
        self.assertEqual(subset_sum(testcase, k), expected)
    


unittest.main()