# 46. Permutations
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # https://medium.com/@ralph-tech/%E6%BC%94%E7%AE%97%E6%B3%95%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98-%E5%9B%9E%E6%BA%AF%E6%B3%95-backtracking-%E5%88%86%E6%94%AF%E5%AE%9A%E7%95%8C%E6%B3%95-branch-and-bound-29165391c377
        # Helper function for backtracking through the list
        def backtrack(start):
            # If the start index reaches the end of the list, a permutation is found
            if start == len(nums):
                # Append a copy of the current permutation to the results
                permutations.append(nums[:])
            else:
                # Iterate over the list to swap each element with the start element
                for i in range(start, len(nums)):
                    # Swap elements at indices start and i
                    nums[start], nums[i] = nums[i], nums[start]
                    # Recursively call backtrack with the next start index
                    backtrack(start + 1)
                    # Swap the elements back to undo the previous swap before the next iteration
                    nums[start], nums[i] = nums[i], nums[start]

        # Initialize an empty list to store all permutations
        permutations = []
        # Start backtracking from the first index
        backtrack(0)
        # Return the list of all permutations found
        return permutations