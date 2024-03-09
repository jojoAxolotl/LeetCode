# 1732. Find the Highest Altitude

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        ans = 0
        cur = 0
        for g in gain:
            cur += g
            ans = max(cur, ans)
        
        return ans   