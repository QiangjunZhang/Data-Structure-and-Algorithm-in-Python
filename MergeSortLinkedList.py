# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        depth = 0
        curr = head
        while curr:
            depth += 1
            curr = curr.next

        def divide(head, depth):
            print('before', head.val, depth)
            leftdepth = 0
            curr = head
            while leftdepth < depth - 1:
                leftdepth += 1
                if leftdepth == depth // 2:
                    lefttail = curr
                    righthead = curr.next
                curr = curr.next
            righttail = curr
            print('after divide', head.val, lefttail.val, righthead.val, righttail.val, depth // 2)
            return head, lefttail, righthead, righttail, depth // 2

        def combine(lefthead, lefttail, righthead, righttail):
            print('to combine', lefthead)
            if lefthead == righthead:
                return lefthead, lefthead
            left = lefthead
            right = righthead
            print('end', righttail.next.val)
            while right != righttail.next:
                if right.val < left.val:
                    lefttail.next = right.next
                    print(lefthead)
                    right.next = left
                    print(lefthead)
                    if left == lefthead:
                        lefthead = right
                        print(lefthead)
                    print('right', right.val)
                    right = lefttail.next
                    print('right', right.val, righttail.next.val, right == righttail.next)
                    print(lefthead)
                else:
                    left = left.next
            print('end of combine', lefthead)
            return lefthead, lefttail

        def sort(head, depth):
            if depth >= 2:
                lefthead, lefttail, righthead, righttail, leftdepth = divide(head, depth)
                lefthead, lefttail = sort(lefthead, leftdepth)
                righthead, righttail = sort(righthead, depth - leftdepth)
                return combine(lefthead, lefttail, righthead, righttail)
            else:
                return head, head

        return sort(head, depth)










