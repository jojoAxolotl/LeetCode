# 450. Delete Node in a BST
# 參考演算法的第七章 Binary Search Tree P16

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]: # type: ignore
        if not root: return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        
        else: # root.val == key
            if not root.left: return root.right # include the case of no child
            if not root.right: return root.left

            if root.left and root.right:
                # find deleteNode's successor
                temp = root.right
                while temp.left: temp = temp.left
                root.val = temp.val
                root.right = self.deleteNode(root.right, root.val)
        
        return root