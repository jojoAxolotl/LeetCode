import heapq
class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        cnt = 0
        while nums and nums[0] < k:
            min_num = heapq.heappop(nums)
            next_min_num = heapq.heappop(nums)
            heapq.heappush(nums, 2*min_num + next_min_num)
            cnt += 1
        return cnt