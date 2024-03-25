# 2352. Equal Row and Column Pairs

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        ans = 0
        for i in range(n): # column
            for j in range(n): # row
                k = 0
                while k < n:
                    if grid[i][k] != grid[k][j]:
                        break
                    k += 1
                    if k == n:  # R[i] == C[j]
                        ans += 1

        return ans