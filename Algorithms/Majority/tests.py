import unittest
from Algorithms.Majority.majorityElement import find_majority


class TestMajority(unittest.TestCase):

    def test_find_majority_element(self):
        nums = [0,0,1,1,1]
        self.assertEqual(find_majority(nums), 4)

        nums = [0,0,1,1,1,0]
        self.assertEqual(find_majority(nums), -1)

        nums = [2,1,1,1,3]
        self.assertEqual(find_majority(nums), 2)