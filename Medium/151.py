# 151. Reverse Words in a String
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        s.reverse()
        s = " ".join(s)
        return s