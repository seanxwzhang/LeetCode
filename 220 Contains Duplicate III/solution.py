# Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
# abs(nums[i] - nums[j]) < t
# abs(i - j) < k

import bisect

class TLESolution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        k = min(k, len(nums) - 1)
        ind = k + 1
        sorted_window = sorted(enumerate(nums[0:ind]), key=lambda i:i[1]) # first k elements
        sorted_map = {sorted_window[i][0]: i for i in xrange(ind)}
        while ind < len(nums):
            if self.ifNearbyExists(sorted_window, t):
                return True
            del sorted_window[sorted_map[ind -k - 1]]
            del sorted_map[ind - k - 1]
            keys = [tup[1] for tup in sorted_window]
            sorted_window.insert(bisect.bisect_left(keys, nums[ind]), (ind, nums[ind]))
            sorted_map = {sorted_window[i][0]: i for i in xrange(len(sorted_window))}
            ind += 1
        return True if self.ifNearbyExists(sorted_window, t) else False

    def ifNearbyExists(self, tuples, t):
        ind = 1
        while ind < len(tuples):
            if abs(tuples[ind][1] - tuples[ind - 1][1]) <= t:
                return True
            ind += 1
        return False

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0: return False
        d, n, w = {}, len(nums), t + 1
        for i in xrange(n):
            key = nums[i] / w
            if key in d:
                return True
            if key - 1 in d and abs(nums[i] - d[key - 1]) < w:
                return True
            if key + 1 in d and abs(nums[i] - d[key + 1]) < w:
                return True
            d[key] = nums[i]
            if i >= k: del d[nums[i - k] / w]
        return False
