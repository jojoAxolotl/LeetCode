# 283. Move Zeroes
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        idx = 0

        for num in nums:
            if num != 0:
                nums[idx] = num
                idx += 1
        for i in range(idx, len(nums)):
            nums[i] = 0
        
        return nums