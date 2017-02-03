#!/usr/bin/env python

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# An O(n) time, O(n) space solution
class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i in xrange(len(nums)):
            if (target - nums[i]) in hashmap:
                return [hashmap[target - nums[i]], i]
            else:
                hashmap[nums[i]] = i

