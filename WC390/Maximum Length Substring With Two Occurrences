# 100245. Maximum Length Substring With Two Occurrences
class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength = 0
        startIdx = 0 # where the substring start
        charCounts = {}  # the dictionary for storing char counts
        
        for endIdx, char in enumerate(s):
            charCounts[char] = charCounts.get(char, 0) + 1 # default is 0
            
            while charCounts[char] > 2:
                charCounts[s[startIdx]] -= 1
                startIdx += 1
            
            maxLength = max(maxLength, endIdx - startIdx + 1)
        
        return maxLength