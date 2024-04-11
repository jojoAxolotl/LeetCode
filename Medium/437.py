# 437. Path Sum III

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
from typing import Optional
from typing import TreeNode

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        d = collections.Counter()
        d[0] = 1
        
        def dfs(node: Optional[TreeNode], s: int) -> int:
            if not node: return 0
            s += node.val
            res =  d[s - targetSum]
            d[s] += 1
            res += dfs(node.left, s) + dfs(node.right, s)
            d[s] -= 1
            if d[s] == 0: del d[s]
            return res
        
        return dfs(root, 0)