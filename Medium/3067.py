# 3067. Count Pairs of Connectable Servers in a Weighted Tree Network
from collections import defaultdict

class Solution(object):
    def countPairsOfConnectableServers(self, edges, signalSpeed):
        """
        :type edges: List[List[int]]
        :type signalSpeed: int
        :rtype: List[int]
        """

        n = len(edges) + 1  # 獲取節點（服務器）的數量
        graph = defaultdict(list)  # 初始化一個默認為列表的字典來存儲圖
        
        # 建立無向圖
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # 定義一個 DFS 函數來計算可連接的節點
        def dfs(u, pre, distance):
            ans = 1 if distance % signalSpeed == 0 else 0
            for v, w in graph[u]:
                if v != pre:  # 避免走回頭路
                    ans += dfs(v, u, (distance + w))
            return ans
        
        # 定義一個函數來計算每個節點可以連接的服務器對的數量
        def count_connectable(u):
            cnt = [dfs(v, u, w) for v, w in graph[u]]
            s = sum(cnt)
            ans = sum(x * (s - x) for x in cnt) // 2
            return ans
        
        # 對每個節點調用 count_connectable 函數並收集結果
        return [count_connectable(u) for u in range(n)]