import sys
# 334. Increasing Triplet Subsequence
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        smallest = sys.maxint
        smaller = sys.maxint
        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= smaller:
                smaller = num
            else:
                return True
        return False