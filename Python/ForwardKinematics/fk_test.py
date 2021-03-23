import unittest
from fk import fk

class TestForwardKinematics(unittest.TestCase):
    def test_forward_kinematics_basic(self):
        # testcase
        arr = [1, 2, 3, 5, 7, 10]
        n = 5
        
        # expected
        expected = 3
        self.assertEqual(binary_search(arr, n), expected)

unittest.main()