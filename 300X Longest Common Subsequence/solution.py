#!/usr/bin/env python
# Solution to the longest common subsequence problem
# Given two lists of characters, return a list of characters that is
# the longest common subsequnce of the two lists
import numpy as np

class Solution(object):
    def solve(self, a, b):
        if not a or not b:
            return []
        l = [[0 for i in xrange(len(a) + 1)] for j in xrange(len(b) + 1)]
        for i in xrange(0, len(b) * 2 - 1):
            x = min(i, len(b) - 1)
            while x >= 0 and i - x < len(a):
                y = i - x
                if b[x] == a[y]:
                    l[x + 1][y + 1] = l[x][y] + 1
                else:
                    l[x + 1][y + 1] = max(l[x][y + 1], l[x + 1][y])
                x -= 1
        tx, ty, res = len(b), len(a), []
        while tx > 0 and ty > 0:
            if l[tx - 1][ty] == l[tx][ty - 1] and l[tx - 1][ty] < l[tx][ty]:
                res = [a[ty - 1]] + res
                tx -= 1
                ty -= 1
            elif l[tx - 1][ty] >= l[tx][ty - 1]:
                tx -= 1
            else:
                ty -= 1
        print(res)
        print(np.matrix(l))
        return l[-1][-1]

if __name__ == "__main__":
    s = Solution()
    print(s.solve(list("ABCDGHHSABDJHABCASY"), list("CEFSABKASDASBDFHR")))

