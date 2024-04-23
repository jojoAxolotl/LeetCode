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
        # 用來記錄從根節點到當前節點的所有可能的總和值，以及每個總和值出現的次數。
        d = collections.Counter()
        d[0] = 1
        
        # depth-first search # s 當前路徑的總和 
        def dfs(node: Optional[TreeNode], s: int) -> int:
            if not node: 
                return 0
            s += node.val
            res =  d[s - targetSum]
            d[s] += 1
            res += dfs(node.left, s) + dfs(node.right, s)
            d[s] -= 1
            if d[s] == 0: 
                del d[s]
            return res
        
        return dfs(root, 0)

'''
求在 binary tree 中找出所有 從任意節點開始到任意節點結束的路徑，使得這些路徑上的節點值的總和 等於 `targetSum`。
解決方案：使用深度優先搜索（DFS）配合一個 Hash Table 表（使用 `collections.Counter`）來跟踪 prefix 及 其出現的次數。
# https://docs.python.org/zh-tw/3/library/collections.html#collections.Counter


1. 初始化計數器：
   - `d` 是一個計數器，用於跟踪從 root 到當前節點的所有可能的總和值，以及每個總和值出現的次數。
   我們初始化 `d[0] = 1` 是因為如果某個節點到根節點的總和剛好是 `targetSum`，那麼我們可以通過這個 prefix 直接獲得一個有效的路徑。

2. DFS 函數：
   - `dfs` 函數遍歷樹的每個節點，並為每個節點更新 prefix 和 `s`。 # s 當前路徑的總和 
   - 對於每個節點，我們首先檢查 `s - targetSum` 是否存在於 `d` 中。這表示從根節點到當前節點的路徑中存在一個或多個子路徑，其總和等於 `targetSum`。
   - 更新 `d[s]`，將當前 prefix 和的計數增加 1，然後遞迴調用左右子節點。
   - 遞迴返回後，為避免影響其他路徑，需將當前節點的 prefix 和的計數減 1。如果某個 prefix 和的計數變為0，則從 `d` 中移除。

3. 時間複雜度：
   - 在最壞的情況下，每個節點都會被訪問一次，因此基本複雜度是 O(N)，其中 N 是樹中的節點數。
   - 在每個節點，我們執行常數時間的操作來更新 `d`。然而，每次更新可能涉及到的查找和插入操作在平均情況下是 O(1)，因為 `Counter` 基於 Hash Table。
   - 然而，注意到在非平衡樹中， prefix 和的數量和變化可能導致更大的操作開銷。如果有許多不同的 prefix 和值，每次查找和更新可能接近 O(logK)，其中 K 是不同 prefix 和的數量。

綜合來看，此代碼的時間複雜度在平均情況下是 O(N)，但在特定情況下，由於哈希表的操作，可能會接近 O(N log K)，取決於樹的結構和節點值的分佈。
'''