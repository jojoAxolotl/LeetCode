# Longest Strictly Increasing or Strictly Decreasing Subarray
from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        lsis = 1 # for Longest Strictly Increasing Subarray
        lsds = 1 # for Longest Strictly Decreasing Subarray
        maximun = 0
        
        drt = None # True: larger, False: less, None: equal
        
        curIdx = 1
        tmpLen = 1
        lastNum = nums[0]
        
        while curIdx < len(nums):
            if drt == None:
                if nums[curIdx] > lastNum:
                    drt = True
                    tmpLen += 1
                elif nums[curIdx] < lastNum:
                    drt = False
                    tmpLen += 1
            elif drt == True:
                if nums[curIdx] > lastNum:
                    tmpLen += 1
                else:
                    lsis = max(lsis, tmpLen)
                    if nums[curIdx] == lastNum:
                        tmpLen = 1
                        drt = None
                    elif nums[curIdx] < lastNum:
                        tmpLen = 2
                        drt = False
            elif drt == False:
                if nums[curIdx] < lastNum:
                    tmpLen += 1
                else:
                    lsds = max(lsds, tmpLen)
                    if nums[curIdx] == lastNum:
                        tmpLen = 1
                        drt = None
                    elif nums[curIdx] > lastNum:
                        tmpLen = 2
                        drt = True
            
            print(curIdx, lastNum, nums[curIdx], drt, tmpLen, lsis, lsds)
            
            lastNum = nums[curIdx]
            curIdx += 1
            
        
        return max (lsis, lsds, tmpLen)
        