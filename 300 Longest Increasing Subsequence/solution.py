# Given an unsorted array of integers, find the length of longest increasing subsequence.

# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

# Your algorithm should run in O(n2) complexity.

# Follow up: Could you improve it to O(n log n) time complexity?

class Solution(object):
    def subOptimalSolution(self, nums):
        l = [None] * len(nums) # l[k] is length of LIS of nums[0:k+1]
        res = 0
        for i, val in enumerate(nums):
            largest = 0
            for j in xrange(i):
                if l[j] > largest and nums[i] > nums[j]:
                    largest = l[j]
            l[i] = largest + 1
            if l[i] > res:
                res = l[i]
        return res

    def optiomalSolution(self, nums):
        aux = [] # aux[i] is the end element [val, length] of the ith active list
        for num in nums:
            # if num is smaller than all current ends, create a new list to the first element
            if not aux or num < aux[0][0]:
                aux = [[num, 1]] + aux
            # if num is greater than all current ends, added a new list to the tail
            elif num > aux[-1][0]:
                aux.append([num, aux[-1][1] + 1])
            # else, search for the flooring element of num, extend it, remove any other list having the same length
            else:


    def lengthOfLIS(self, nums):
        return self.subOptimalSolution(nums)

if __name__ == "__main__":
    s = Solution()
    r = s.lengthOfLIS([10,9,2,5,3,7,101,18,33,2,41,23,15])
    print(r)


