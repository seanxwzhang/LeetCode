# Numbers can be regarded as product of its factors. For example,

# 8 = 2 x 2 x 2;
#   = 2 x 4.
# Write a function that takes an integer n and return all possible combinations of its factors.

# Note: 
# You may assume that n is always positive.
# Factors should be greater than 1 and less than n.
# Examples: 
# input: 1
# output: 
# []
# input: 37
# output: 
# []
# input: 12
# output:
# [
#   [2, 6],
#   [2, 2, 3],
#   [3, 4]
# ]
# input: 32
# output:
# [
#   [2, 16],
#   [2, 2, 8],
#   [2, 2, 2, 4],
#   [2, 2, 2, 2, 2],
#   [2, 4, 4],
#   [4, 8]
# ]

class Solution(object):
    def getFactors(self, n):
        return self.backtrack([], n, [])

    def backtrack(self, res, n, prefix):
        factor = 2
        while factor * factor <= n:
            if n % factor == 0 and (len(prefix) == 0 or prefix[len(prefix) - 1] <= factor): # if factor is indeed a factor
                prefix.append(factor)
                res.append(prefix + [n / factor])
                self.backtrack(res, n / factor, prefix)
                prefix.pop()
            factor += 1
        return res
                
s = Solution()
print(s.getFactors(32))