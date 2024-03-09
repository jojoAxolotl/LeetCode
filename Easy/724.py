# 724. Find Pivot Index
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = sum(nums) - nums[0]
        for idx in range(len(nums)):
            if left == right:
                return idx
            else:
                left += nums[idx]
                if idx + 1 < len(nums):
                    right -= nums[idx+1]
        return -1