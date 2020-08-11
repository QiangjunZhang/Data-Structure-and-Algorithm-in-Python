# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1 + val2 + carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next

def genList(list):
    L = [None]*len(list)
    for n in range(len(list)):
        if n == 0:
            L[n] = ListNode(list[n])
        else:
            L[n] = ListNode(list[n])
            L[n].next = L[n-1]

    return L[-1]


def main():
    # l1 = genList([2, 3, 4])
    # l2 = genList([5, 6, 4])
    # x = Solution()
    # sum = x.addTwoNumbers(l1, l2)
    # print(sum)

    # l1 = ListNode(0)
    # l2 = l1
    # l1.next = ListNode(2)
    #
    # print((l1.next).val)
    #
    # x = [1,2,3]
    # y = x
    # y.append(23)
    # print(x)

    x= ' '
    sub = x[0]
    
    print(len(x))
if __name__ == '__main__':
    main()