#!/usr/bin/env python

# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

# Your algorithm should run in O(n) complexity.


class Solution(object):

    def longestConsecutive(self, nums):
        nums = set(nums)
        best = 0
        for i in nums:
            if (i - 1) not in nums:
                j = i 
                while j in nums:
                    j += 1
                best = max(best, j - i)
        return best


# TODO: the following union find algorithm does not work due to too many recursion
class Solution1(object):
    def __init__(self):
        self.dd = {} # {100: [representative, number of consecutive elements]}
        self.res = 0

    def findRepresentative(self, ind):
        if ind not in self.dd:
            return None
        if ind == self.dd[ind][0]: # if a number's representative is itself
            return self.dd[ind]
        rep = self.findRepresentative(self.dd[ind][0])
        self.dd[ind][0] = rep[0]
        return rep

    def longestConsecutive(self, nums):
        nums = set(nums)
        for num in nums:
            left = self.findRepresentative(num - 1)
            right = self.findRepresentative(num + 1)
            if not left and not right:
                self.dd[num] = [num, 1]
            elif not left:
                self.dd[num] = [num, right[1] + 1]
                right[0] = num
            elif not right:
                self.dd[num] = [num, left[1] + 1]
                left[0] = num
            elif left[0] != right[0]:
                self.dd[num] = [num, left[1] + right[1] + 1]
                left[0] = num
                right[0] = num
            self.res = max(self.res, self.dd[num][1])
        return self.res


if __name__ == "__main__":
    s = Solution()
    nums = [1,2,0,1]
    print(s.longestConsecutive(nums))
