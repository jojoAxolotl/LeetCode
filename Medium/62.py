class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1]*m for _ in range(n)]
        def up(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            if i == 0 or j == 0:
                return 1
            else:
                dp[i][j] = up(i-1, j) + up(i, j-1)
                return dp[i][j]
        return up(n-1, m-1)