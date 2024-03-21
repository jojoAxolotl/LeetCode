# 1207. Unique Number of Occurrences
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        num_occ = {}
        for num in arr:
            if num in num_occ:
                num_occ[num] += 1
            else:
                num_occ[num] = 1
        
        if len(num_occ) == len(set(num_occ.values())):
            return True
        return False