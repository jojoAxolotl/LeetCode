# 80. Remove Duplicates from Sorted Array II
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        count = 0
        while j < len(nums):
            if nums[i] == nums[j]:
                count += 1
                if count > 1:
                    while(j < len(nums) and nums[i] == nums[j]):
                        nums.remove(nums[j])
                else:
                    j += 1
                    continue
            i = j
            j = i + 1
            count = 0
        return len(nums)