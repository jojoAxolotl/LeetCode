# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = righ
t
from typing import Optional
from typing import TreeNode

# Sol 1 : original
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def countGoodNodes(greatest, node):
            if not node:
                return 0  # Base case: if the node is None, return 0

            # If the current node's value is greater than or equal to the greatest value seen so far,
            # it is a good node. Update the greatest value for subsequent recursive calls if necessary.
            
            if node.val >= greatest:
                curCount = 1  # This node is good, so count it
                greatest = node.val  # Update greatest since this node's value is greater
            else:
                curCount = 0  # This node is not good, do not count it

            # Recursively count good nodes in the left and right subtrees.
            # Pass the updated greatest value to these calls.
            leftCount = countGoodNodes(greatest, node.left)
            rightCount = countGoodNodes(greatest, node.right)

            # The total count for the current subtree is the sum of good nodes in left and right subtrees,
            # plus the current node if it's good.
            return curCount + leftCount + rightCount

        # Initial call starts with the root's value as the greatest seen so far.
        return countGoodNodes(root.val, root)

# Sol 2 DFS
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, greatest):
            if not node:
                return 0
            count = 1 if node.val >= greatest else 0
            greatest = max(greatest, node.val)
            count += dfs(node.left, greatest)
            count += dfs(node.right, greatest)
            return count
        
        return dfs(root, root.val)