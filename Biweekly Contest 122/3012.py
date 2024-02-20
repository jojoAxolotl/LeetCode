# 3012. Minimize Length of Array Using Operations

# Intuition
# The order of elements doesn't matter.
# We should avoid of picking A[i] == A[j], because it will generate 0.
# KEY IDEA! If we have A[i] < A[j], then we can remove A[j]

# Solution: 
# any num > min(A), is eliminated by min(A).
# all min(A)'s are eliminated by num % min(A) 
# since it is smaller than v. -> return 1
# Otherwise, count min(A) in A, and return (cnt + 1) / 2

# Time O(n) & Space O(1)

class Solution(object):
    def minimumArrayLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum = min(nums)
        for num in nums:
            if num % minimum > 0:
                return 1
        return (nums.count(minimum)+1)//2