import unittest
from Algorithms.Kadanes.maxSubarray import max_sub_array


class TestJumpGame(unittest.TestCase):

    def test_max_sub_array(self):
        arr = [-2,1,-3,4,-1,2,1,-5,4]
        self.assertEqual(max_sub_array(arr), 6)


if __name__ == '__main__':
    unittest.main()