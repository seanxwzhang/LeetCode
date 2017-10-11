# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

# Each number in C may only be used once in the combination.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
# A solution set is: 
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]

class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        table = [set() for _ in xrange(target + 1)]
        for num in candidates:
            if num > target:
                break
            for j in xrange(target - num, 0, -1):
                table[num + j] |= {elt + (num,) for elt in table[j]}
            table[num].add((num,))
        return map(list, table[target])

candidates = [10,1,2,7,6,1,5]
target = 8
s = Solution()
print(s.combinationSum2(candidates, target))