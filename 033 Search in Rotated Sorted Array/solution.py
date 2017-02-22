#! /usr/bin/env python
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.


class Solution(object):
    def search(self, nums, target):
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while(left < right):
            mid = (left + right) / 2
            if (nums[mid] > nums[right]):
                left = mid + 1
            else:
                right = mid
        smallest, l, r = left, 0, len(nums) - 1
        while l <= r:
            mid = (l + r) / 2
            realmid = (mid + smallest) % len(nums)
            if (nums[realmid] == target):
                return realmid
            elif (nums[realmid] < target):
                l = mid + 1
            else:
                r = mid - 1
        return -1
        

if __name__ == "__main__":
    s = Solution()
    print(s.search([1], 2))