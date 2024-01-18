# 1431. Kids With the Greatest Number of Candies
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        largest = 0
        rtList = [False] * len(candies)
        
        for i in candies:
            if i > largest:
                largest = i
        
        for i in range(len(candies)):
            if candies[i] + extraCandies >= largest:
                rtList[i] = True
        
        return rtList