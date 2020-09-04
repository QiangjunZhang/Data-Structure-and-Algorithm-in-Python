import unittest
from Algorithms.LineSweeping.mergeIntervals import MergeIntervals


class TestMergeIntervals(unittest.TestCase):

    def test_merge_intervals(self):
        intervals = MergeIntervals([[1,3],[2,6],[8,10],[15,18]])
        expected = [[1,6],[8,10],[15,18]]
        self.assertEqual(intervals.merge(), expected)

        intervals = MergeIntervals([[1,4],[4,5]])
        expected = [[1,5]]
        self.assertEqual(intervals.merge(), expected)
