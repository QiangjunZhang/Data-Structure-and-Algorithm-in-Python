# Definition for a binary tree node.
from typing import List
import copy
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def backtrack(node):
            # choose one of three options
            # print(node.val, k)
            if self.count == n:
                # ans = beforeOrder(root)
                result.append(copy.deepcopy(root))
            if n - self.count > 0:
                node.left = TreeNode(0)
                self.count += 1
                backtrack(node.left)
                node.left = None
                self.count -= 1
                node.right = TreeNode(0)
                self.count += 1
                backtrack(node.right)
                node.right = None
                self.count -= 1
            if n - self.count > 1:
                node.left = TreeNode(0)
                node.right = TreeNode(0)
                self.count += 2
                if self.count == n:
                    backtrack(node.left)
                    self.count -= 2
                    node.right = None
                    node.left = None
                else:
                    backtrack(node.left)
                    backtrack(node.right)
                    self.count -= 2
                    node.right = None
                    node.left = None

        def inOrder(node):
            if node.left:
                inOrder(node.left)
            node.val = self.n
            self.n += 1
            if node.right:
                inOrder(node.right)

        result = []
        self.count = 1
        root = TreeNode(1)
        backtrack(root)

        for node in result:
            self.n = 1
            inOrder(node)
        return result

result = Solution().generateTrees(5)
print(result)
