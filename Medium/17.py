# 17. Letter Combinations of a Phone Number

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        rt = []
        digitTF = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        # like tree structure
        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                rt.append(curStr)
                return
            for c in digitTF[digits[i]]:
                backtrack(i+1, curStr+c)
        
        if digits:
            backtrack(0, "")

        return rt