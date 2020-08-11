from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def mergeTwoLists(L1, L2):
            dummy = ListNode()
            curr = dummy
            while L1 and L2:
                if L1.val <= L2.val:
                    curr.next = L1
                    curr = curr.next
                    L1 = L1.next
                else:
                    curr.next = L2
                    curr = curr.next
                    L2 = L2.next
            if L1: curr.next = L1
            if L2: curr.next = L2
            return dummy.next

        if not lists: return None

        while len(lists) > 1:
            l = 0
            r = len(lists) - 1
            curr = []
            while l <= r:
                if l == r:
                    curr.append(lists[l])
                else:
                    curr.append(mergeTwoLists(lists[l], lists[r]))
                l += 1
                r -= 1
            lists = curr

        return lists[0]