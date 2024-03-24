# 100228. Apply Operations to Make Sum of Array Greater Than or Equal to k
from math import floor, sqrt
class Solution(object):
    def minOperations(self, k):
        """
        :type k: int
        :rtype: int
        """
        i = floor(sqrt(k))
        if i * i >= k:
            return int(2*i-2)
        elif (i+1) * i >= k:
            return int(2*i-1)
        elif (i+1) * (i+1) >= k:
            return int(2*i)