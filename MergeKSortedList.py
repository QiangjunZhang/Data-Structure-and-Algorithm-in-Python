from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        class minHeap():

            def __init__(self, hplist):
                self.hplist = []
                self.size = 0
                for l in hplist:
                    self.add(l)

            def _parent(self, i):
                return (i - 1) // 2

            def _left_child(self, i):
                return 2 * i + 1

            def _right_child(self, i):
                return 2 * i + 2

            def has_left(self, i):
                return 2 * i + 1 < self.size

            def has_right(self, i):
                return 2 * i + 2 < self.size

            def is_root(self, i):
                return i == 0

            def swap(self, i, j):
                self.hplist[i], self.hplist[j] = self.hplist[j], self.hplist[i]

            def add(self, element):
                self.size += 1
                self.hplist.append(element)
                self.upheap(self.size - 1)

            def upheap(self, i):
                parent = self._parent(i)
                if i > 0 and self.hplist[i][0] < self.hplist[parent][0]:
                    self.swap(i, parent)
                    self.upheap(parent)

            def push(self):
                self.swap(0, self.size - 1)
                discarded = self.hplist.pop()
                self.size -= 1
                self.downheap(0)
                return discarded

            def downheap(self, i):
                if self.has_left(i):
                    left_child = self._left_child(i)
                    small_child = left_child

                    if self.has_right(i):
                        right_child = self._right_child(i)
                        if self.hplist[right_child][0] < self.hplist[left_child][0]:
                            small_child = right_child

                    if self.hplist[i][0] > self.hplist[small_child][0]:
                        self.swap(i, small_child)
                        self.downheap(small_child)
        # for i in range(len(lists)):
        #     list[i]
        initial = []
        for i in range(len(lists)):
            if lists[i] != None:
                initial.append((lists[i].val, i))

        minHeapList = minHeap(initial)

        result = ListNode(0)
        ans = result
        while minHeapList.size != 0:
            # push the min_melement into the result list
            min_element = minHeapList.push()
            ans.next = ListNode(min_element[0])
            # position at the tail of the result list
            ans = ans.next
            # add one more element into the heap
            n = min_element[1]
            if lists[n].next != None:
                minHeapList.add((lists[n].next.val, n))
                # m move the pointer of the selected list
                lists[n] = lists[n].next

        return result.next

def main():
    list1 = ListNode(0)
    list1.next = ListNode(1)
    # list1.next.next = ListNode(2)

    list2 = ListNode(2)
    list2.next = ListNode(3)
    # list2.next.next = ListNode(4)

    lists= [list1, None]

    x= Solution()
    result = x.mergeKLists(lists)
    while result != None:
        print(result.val)
        result = result.next
    # print(result.val, )

def test():
    A = ListNode(1)
    B = ListNode(2)
    C = ListNode(3)
    A.next = B
    B.next = C

    A.next = C
    B.next = A
    return B
    # pass

if __name__ == '__main__':
    # main()
    B = test()








