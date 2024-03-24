class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # check any amount of num in nums less than or equal to 2
        amount = {}
        for num in nums:
            if num in amount:
                amount[num] += 1
                if amount[num] > 2:
                    return False
            else:
                amount[num] = 1
        return True   