# 27. Remove Element
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        front = 0
        end = len(nums) - 1
        k = 0
        while front <= end:
            if nums[front] != val:
                front = front + 1
                k = k + 1
            else:
                if nums[end] != val:
                    nums[front] = nums[end]
                    end = end - 1
                    front = front + 1
                    k = k + 1
                else:
                    end = end - 1
        return k