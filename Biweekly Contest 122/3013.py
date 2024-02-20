# 3013. Divide an Array Into Subarrays With Minimum Cost II
# 還是不會貓貓ＱＱ

class Solution(object):
    def minimumCost(self, nums, k, dist):
        """
        :type nums: List[int]
        :type k: int
        :type dist: int
        :rtype: int
        """
        
        """
        dist = n -> list's length = n + 1
        k = m -> find (m - 1)'s smallest numbers
        """
        '''
        find amount smallest numbers in an list
        '''
        def _helper1(amount, sublist):
            small = []
            for i in range(amount):
                small += [sublist[i]]
            if len(sublist) > amount:
                for i in range(amount, len(sublist)):
                    for j in range(amount):
                        if sublist[i] < small[j]:
                            small.sort()
                            small[-1] = sublist[i]
                            break
            return sum(small)
        
        smallest = 100000000
        length = dist+1
        amount = k-1
        
        for i in range(1, len(nums)-length):
            small = _helper1(amount, nums[i: i+length])
            if small < smallest:
                smallest = small
        return smallest + nums[0]

class Solution(object):
    def minimumCost(self, nums, k, dist):
        n = len(nums)
        # dp[i][j] 表示分割前 i 个元素成 j 个子数组的最小成本
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                for x in range(max(0, i - dist - 1), i):
                    dp[i][j] = min(dp[i][j], dp[x][j - 1] + nums[x])
        
        return dp[n][k]
