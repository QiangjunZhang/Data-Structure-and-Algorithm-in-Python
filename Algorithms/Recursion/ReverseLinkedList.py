# Recursion
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SolutionRec:
    def reverseList(self, head):
        return self._reverse(head)

    def _reverse(self, curr, prev=None):
        if not curr:
            return prev
        after = curr.next
        curr.next = prev
        return self._reverse(after, curr)


# Iteration
class SolutionIte:
    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
