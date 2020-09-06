import unittest
from Algorithms.PrefixSum.prefixSum import solver


class TestPrefixSum(unittest.TestCase):

    def test_prefix_sum(self):
        S = 'CAGCCTA'
        P = [2, 5, 0]
        Q = [4, 5, 6]
        expected = [2, 4, 1]
        self.assertEqual(solver(S, P, Q), expected)

        P = [2, 5, 4]
        Q = [4, 5, 5]
        expected = [2, 4, 2]
        self.assertEqual(solver(S, P, Q), expected)
