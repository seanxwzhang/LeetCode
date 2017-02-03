# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.


class Solution(object):
    def climbStairs(self, n):
        nums = [1, 2]
        for i in xrange(2, n):
            nums.append(nums[i - 2] + nums[i - 1])
        return nums[n - 1]
            