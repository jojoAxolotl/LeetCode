# 2390. Removing Stars From a String
# https://walkccc.me/LeetCode/problems/2390/#__tabbed_1_3

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        # stack
        ans = []
        for char in s:
            if char == '*':
                ans.pop()
            else:
                ans.append(char)
        return ''.join(ans)