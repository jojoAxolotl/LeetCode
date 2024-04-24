# 199. Binary Tree Right Side View
# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
from collections import defaultdict, deque
from typing import TreeNode,List 


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans

        q = deque([(0, root)])
        mp = defaultdict(int)

        while q:
            horiz, node = q.popleft()

            if horiz not in mp:
                mp[horiz] = node.val

            if node.right:
                q.append((horiz + 1, node.right))
            if node.left:
                q.append((horiz + 1, node.left))

        for val in mp.values():
            ans.append(val)

        return ans