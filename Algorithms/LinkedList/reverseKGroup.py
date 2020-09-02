class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        1 -  2  - 3
        prev curr next

        1 < 2    3
            prev curr
        """

        def reverse(head, tail):
            end = tail.next
            new_tail = head
            prev = head
            curr = head.next
            while curr != end:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev, new_tail

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        fast = head
        slow = head
        count = k
        while fast:
            fast = fast.next
            count -= 1
            if count == 1 and fast:
                next = fast.next
                new_head, new_tail = reverse(slow, fast)
                prev.next = new_head
                new_tail.next = next
                prev = new_tail
                fast = next
                slow = next
                count = k
        return dummy.next









