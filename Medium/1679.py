# 1679. Max Number of K-Sum Pairs
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        '''
        # attempt 1: can use but too slow
        
        op = 0
        
        # this acceleration is not enough
        for i in nums:
            if i >= k:
                nums.remove(i)
        
        while nums != []:
            check = nums[0]
            checkExist = k - check
            for i in nums[1:]:
                if i == checkExist:
                    op += 1
                    nums.remove(i)
                    break
            nums.remove(check)
        return op
        '''

        # attempt 2: use dictionary
        op = 0
        num_count = {}  # 使用字典來記錄數字的出現次數

        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1

        for n in num_count:
            tmp = k - n
            if n == tmp:
                op += num_count[n] // 2  
            elif n < tmp and tmp in num_count:
                op += min(num_count[n], num_count[tmp])
        
        return op