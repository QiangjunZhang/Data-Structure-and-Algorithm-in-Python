# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: Node) -> int:
        self.ans = 0

        def depth(node):
            if not node: return 0
            """do the recursive call before the if statement is necessary 
            so the search will loop all the nodes"""
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            R = L = 0
            if node.left and node.val == node.left.val:
                L = left_depth + 1
            if node.right and node.val == node.right.val:
                R = right_depth + 1
            self.ans = max(self.ans, L + R)
            return max(L, R)

        depth(root)
        return self.ans


def main():
    s = [1,4,5,4,4,5]
    root = Node(1)
    root.left = Node(4)
    root.right = Node(5)
    root.left.left = Node(4)
    root.left.right = Node(4)
    root.right.left = Node(5)

    x = Solution()
    result = x.longestUnivaluePath(root)
    print(result)


if __name__ == '__main__':
    main()
