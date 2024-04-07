# Minimum Operations to Make Median of Array Equal to K
from typing import List


class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        midPlace = len(nums) // 2
        nums = sorted(nums)
        cnt = 0

        print(midPlace, nums[midPlace], k)
        
        if nums[midPlace] > k:
            idx = midPlace
            while 0 <= idx < len(nums) and nums[idx] > k:
                cnt += (nums[idx] - k)
                idx -= 1
        elif nums[midPlace] < k:
            idx = midPlace
            while 0 <= idx < len(nums) and nums[idx] < k:
                cnt += (k - nums[idx])
                idx += 1
        
        return cnt