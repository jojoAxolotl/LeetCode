# 1768. Merge Strings Alternately
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        cur = 0
        merge = ''

        while cur < len(word1) and cur < len(word2):
            merge = merge + word1[cur] + word2[cur]
            cur += 1

        if cur < len(word1):
            merge = merge + word1[cur:]

        if cur < len(word2):
            merge = merge + word2[cur:]
        
        return merge