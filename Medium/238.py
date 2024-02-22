# 238. Product of Array Except Self
import copy
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        answer[i] is equal to the product of all the elements of nums except nums[i]
        """
        '''
        # 1st attempt: time complexity O(n^2)
        def _helper(nums):
            ans = 1
            for num in nums:
                ans = ans * num
            return ans

        answer = [0]*len(nums)

        for idx, num in enumerate(nums):
            temp = copy.deepcopy(nums)
            temp.remove(temp[idx])
            answer[idx] = _helper(temp)
            
        return answer
        '''
        # 2nd: prefix (all left side) and suffix (all right side)
        # References: https://weikaiwei.com/algorithm/leetcode-238/

        answer = [0]*len(nums)
        prefix = [0]*len(nums)
        suffix = [0]*len(nums)

        # for suffix
        suffix_temp = 1
        for idx, num in enumerate(nums):
            suffix[idx] = suffix_temp
            suffix_temp = suffix_temp * num
        

        # for prefix
        nums.reverse()
        prefix_temp = 1
        for idx, num in enumerate(nums):
            prefix[idx] = prefix_temp
            prefix_temp = prefix_temp * num
        prefix.reverse()
        
        # for answer
        # print(prefix)
        # print(suffix)
        for idx in range(len(answer)):
            answer[idx] = prefix[idx] * suffix[idx]
        return answer