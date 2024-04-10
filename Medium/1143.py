# 1143. Longest Common Subsequence
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # LCS is a standard question for DP
        n=len(text1)
        m=len(text2)
        dp=[[-1]*m for _ in range(n)]
        def lcs(i, j):
            nonlocal dp
            if i>=n or j>=m:  
                return 0
            if dp[i][j]!=-1: 
                return dp[i][j] # DP 的部分
            if text1[i]==text2[j]:
                dp[i][j]=1+lcs(i+1, j+1)
                return dp[i][j]
            else:
                dp[i][j]= max(lcs(i, j+1), lcs(i+1, j))
                return dp[i][j]
        return lcs(0, 0)