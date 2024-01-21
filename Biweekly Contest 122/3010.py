# 3010. Divide an Array Into Subarrays With Minimum Cost I
class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = nums[0]
        small1 = nums[1]
        small2 = nums[2]
        
        if len(nums) > 3:
            for i in range(3, len(nums)):
                if nums[i] < small1 or nums[i] < small2:
                    if small1 < small2:
                        small2 = nums[i]
                    else:
                        small1 = nums[i]
        
        total += small1 +  small2
        return total