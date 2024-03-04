# 3066. Minimum Operations to Exceed Threshold Value II
class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Runtime Error
        
        cnt = 0
        while min(nums) < k:
            cnt += 1
            nums.sort()
            for idx, num in enumerate(nums):
                if num >= k:
                    nums = nums[:idx+1]
            
            x = nums[0]
            y = nums[1]
            
            del nums[0]
            del nums[0]
            
            nums.append(min(x, y) * 2 + max(x, y))
        return cnt