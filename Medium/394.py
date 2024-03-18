# 394. Decode String
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s:
            stack.append(char)

            if char == "]":
                stack.pop(-1) # for pop "]"
                letter = []
                while stack[-1] != "[":
                    letter.append(stack[-1])
                    stack.pop(-1)
                letter = letter[::-1] # reverse
                letter_str = "".join(letter)
                stack.pop(-1) # for pop "["

                num = ""
                while not stack[-1].isalpha() and stack[-1] != "[":
                    num += stack[-1]
                    stack.pop(-1)
                    if len(stack) == 0:
                        break # finish by no additional char(s)
                num = num[::-1]

                repeat = ""
                for i in range(int(num)):
                    repeat += letter_str
                stack.append(repeat)

        return "".join(stack) # finish by additional char(s)