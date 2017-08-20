#!/usr/bin/env python
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place, do not allocate extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# Brute force: find all permutation, then find the next greater permutation, complexity O(n!)
# Essentially we need to find:
# 1. An index i indicating the first difference between original permutation and current permutation
#    original[i] < current[i]
# 2. current[i:] should be the smallest permutation possible
# 3. index i should be the largest possible
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 2, -1, -1):
          swapCandidates = [j for j in range(i + 1, len(nums)) if nums[j] > nums[i]]
          if len(swapCandidates) > 0:
            bestSwap = swapCandidates.sort(key=lambda j: nums[j])[0]
            candidates = sorted([nums[x] for x in range(i, len(nums)) if x != bestSwap])
            return nums[:i] + candidates
