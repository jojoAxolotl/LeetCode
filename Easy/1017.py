# 1071. Greatest Common Divisor of Strings
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def _divisor(str, div):
            """
            :type str: str
            :type div: str
            :rtype: T/F
            str and divided by div or not
            """
            if len(str) % len(div) == 0:
                if str == div * (len(str)/len(div)):
                    return True
            return False
        
        if str1 >= str2:
            div = str2
        else:
            div = str1

        while div != "":
            if _divisor(str1, div) and _divisor(str2, div):
                return div
            div = div[:-1]
        return ""