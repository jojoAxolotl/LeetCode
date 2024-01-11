# 26. Remove Duplicates from Sorted Array
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        while k <= len(nums) - 1:
            if nums[k-1] == nums[k]:
                nums.remove(nums[k-1])
                k -= 1
            k += 1
        return len(nums)

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1