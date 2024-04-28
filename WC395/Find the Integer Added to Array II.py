# 100287. Find the Integer Added to Array II
from typing import List

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        
        from itertools import combinations
        nums1.sort()
        nums2.sort()
        n1 = len(nums1)
        n2 = len(nums2)
        minimum_x = float('inf')  # Start with a large number to find the minimum

        # Iterate over all combinations of indices to be removed from nums1
        # 遍歷 nums1 中所有可能的兩個 index 組合。為了找到刪除哪兩個元素後，剩餘的列表元素可以通過增加一個固定的數 x 與 nums2 匹配。
        for indices in combinations(range(n1), 2):
            # Create a new list without the two selected elements
            modified_nums1 = [nums1[i] for i in range(n1) if i not in indices]

            # Calculate the potential x for this configuration
            potential_xs = [nums2[i] - modified_nums1[i] for i in range(n2)]

            # Check if all values of x are the same, since we need consistent transformation
            if all(x == potential_xs[0] for x in potential_xs):
                # Update the minimum x if the found x is smaller
                minimum_x = min(minimum_x, potential_xs[0])

        return minimum_x