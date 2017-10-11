class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        k = min(k, len(nums) - 1)
        ind = k + 1
        window = set(nums[0:ind]) # [0,1,2,3...,k]
        while ind < len(nums):
            window.remove(nums[ind - k - 1])
            window.add(nums[ind])
            ind += 1
            if len(window) != k + 1:
                return True
        return True if len(window) != k + 1 else False
