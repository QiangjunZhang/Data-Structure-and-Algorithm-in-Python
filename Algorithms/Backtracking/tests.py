import unittest
from Algorithms.Backtracking.combinationSum import CombinationSum


class TestCombinationSum(unittest.TestCase):
    def test_combination_sum(self):
        obj = CombinationSum([10, 1, 2, 7, 6, 1, 5])
        expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        self.assertEqual(obj.combinationSum(8), expected)

        obj = CombinationSum([2, 5, 2, 1, 2])
        expected = [[1, 2, 2], [5]]
        self.assertEqual(obj.combinationSum(5), expected)


if __name__ == '__main__':
    unittest.main()
