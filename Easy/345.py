# 345. Reverse Vowels of a String
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = "aeiouAEIOU"
        s_list = list(s)

        index = []
        chars = []

        for i, char in enumerate(s_list):
            if char in vowels:
                index.append(i)
                chars.append(char)

        chars.reverse()

        for i, char_index in enumerate(index):
            s_list[char_index] = chars[i]

        return ''.join(s_list)