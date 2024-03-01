# 11. Container With Most Water
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # linear time sol O(n)
        
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return res