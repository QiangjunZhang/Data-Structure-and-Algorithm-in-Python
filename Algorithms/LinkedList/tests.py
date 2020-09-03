import unittest
import Algorithms.LinkedList.reverseKGroup as Solver
from Algorithms.LinkedList.reverseKGroup import ListNode


class TestStringMethods(unittest.TestCase):
    def test_reverse(self):
        head = ListNode(0)
        curr = head
        for val in [1, 2, 3, 4, 5, 6]:
            curr.next = ListNode(val)
            curr = curr.next

        head_rev = ListNode(0)
        curr = head_rev
        for val in [2, 1, 4, 3, 6, 5]:
            curr.next = ListNode(val)
            curr = curr.next
        k = 2
        solver = Solver.Solution()
        test = solver.reverseKGroup(head.next, k)
        expected = head_rev.next
        while test and expected:
            self.assertEqual(test.val, expected.val)
            test = test.next
            expected = expected.next


if __name__ == '__main__':
    unittest.main()
