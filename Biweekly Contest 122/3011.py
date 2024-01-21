# 3011. Find if Array Can Be Sorted
class Solution(object):
    def canSortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
        to count the set bit of the input number
        '''
        def _helper(num):
            if num // 2 == 0:
                return num
            else:
                return num % 2 + _helper(num // 2)
        '''
        check different set bit's numbers is sorted 
        '''
        setBit = []
        for num in nums:
            setBit += [_helper(num)]
        # print(setBit) # correct!
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if setBit[i] != setBit[j]:
                    if i < j:
                        if (nums[i]<nums[j]) == False:
                            return False
                    if i > j:
                        if (nums[i]>nums[j]) == False:
                            return False
        return True