# 700. Search in a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]: # type: ignore
        def _helper(root, val):
            curVal = root.val
            if curVal == val:
                return root
            elif curVal > val and root.left != None:
                return _helper(root.left, val)
            elif curVal < val and root.right != None:
                return _helper(root.right, val)
            else:
                return None
        return _helper(root, val)