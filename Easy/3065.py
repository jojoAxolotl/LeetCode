# 3065. Minimum Operations to Exceed Threshold Value I
class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt = 0
        for num in nums:
            if num < k:
                cnt += 1
        return cnt