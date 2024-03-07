# 1493. Longest Subarray of 1's After Deleting One Element
# https://kevinchung0921.medium.com/leetcode-%E8%A7%A3%E9%A1%8C%E7%B4%80%E9%8C%84-1493-longest-subarray-of-1s-after-deleting-one-element-dc9fde5864d9
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zeroSeen = False
        prev, curr = 0, 0
        max_len = 0
        for n in nums:
            if n == 1:
                curr += 1  # Continue counting the current streak of 1s
            else:
                max_len = max(max_len, curr + prev)  # Check if this is the longest subarray upon seeing a 0
                prev = curr  # Assign the length of the current streak of 1s to prev
                curr = 0     # Reset current streak of 1s
                zeroSeen = True  # Mark that a 0 has been seen
        max_len = max(max_len, curr + prev)  # Check the length one more time to cover cases where the last number isn't 0
        # Adjust the return value based on whether a 0 was seen. If no 0 seen, all are 1s, subtract one to delete one element.
        return max_len if zeroSeen else max_len - 1 