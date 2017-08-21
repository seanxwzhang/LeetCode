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

    # Find the index of the largest element in arr that's smaller than than target
    # Prerequisite: there exists such element
    def biSearch(self, arr, target):
        print('searching %d' % target)
        l, r = 0, len(arr) - 1
        while (r - l) > 1:
            m = l + (r - l) / 2
            print('arr[%d] is %d, arr[%d] is %d, arr[%d] is %d' % (l, arr[l], r, arr[r], m,  arr[m]))
            if arr[m] < target:
                l = m
            else:
                r = m
        return r

    def optiomalSolution(self, nums):
        aux = [] # aux[i] is the end element [val, length] of the ith active list
        for num in nums:
            print(aux)
            if not aux:
                aux = [num]
            # if num is smaller or equal to all current ends, create a new list to the first element
            elif num <= aux[0]:
                aux[0] = num
            # if num is greater than all current ends, added a new list to the tail
            elif num > aux[-1]:
                aux.append(num)
            # else, search for the flooring element of num, extend it, remove any other list having the same length
            else:
                index = self.biSearch(aux, num)
                print('index is %d' % index)
                aux[index] = num
        return len(aux)

    def lengthOfLIS(self, nums):
        return self.optiomalSolution(nums)

if __name__ == "__main__":
    s = Solution()
    r = s.lengthOfLIS([4,10,4,3,8,9])
    print(r)

