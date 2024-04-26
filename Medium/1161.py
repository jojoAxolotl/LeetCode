# 1161. Maximum Level Sum of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import Optional


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int: # type: ignore
        minLevel = 1
        maxSum = float('-inf')

        # Appendix: https://wiki.python.org/moin/TimeComplexity
        queue = deque()
        queue.append(root)

        level = 1

        while queue:
            levelSum = 0
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                levelSum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if levelSum > maxSum:
                maxSum = levelSum
                minLevel = level
            
            level += 1
        return minLevel