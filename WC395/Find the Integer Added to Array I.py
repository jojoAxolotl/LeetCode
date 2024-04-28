# 100285. Find the Integer Added to Array I
from typing import List

class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_min = min(nums1)
        nums2_min = min(nums2)
        return nums2_min - nums1_min