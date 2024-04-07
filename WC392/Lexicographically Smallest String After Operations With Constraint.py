# Lexicographically Smallest String After Operations With Constraint
class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        s_list = list(s)
        n = len(s_list)
        
        for i in range(n):
            # calculate the cyclic distance to 'a' from the current character
            # the cyclic distance considers the direct path and the wrap-around path
            distance_direct = ord(s_list[i]) - ord('a')
            distance_wrap = ord('z') - ord(s_list[i]) + 1
            distance = min(distance_direct, distance_wrap)

            # if changing it to 'a' does not exceed k, do it
            if distance <= k:
                k -= distance
                s_list[i] = 'a'
            else:
                s_list[i] = chr(ord(s_list[i]) - k)
                k = 0  # all available 'k' has been used.
            
            # if k is completely used up, no further changes can be made.
            if k == 0:
                break

        return ''.join(s_list)