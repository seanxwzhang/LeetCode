# basically leetcode 40


class Solution(object):
    def divide(self, l):
        return map(lambda x: float(x)/100, l)

    def combinationSum2(self, candidates, target):
        candidates = map(lambda x: int(100 * x), candidates)
        target = int(100 * target)
        candidates.sort()
        table = [set() for _ in xrange(target + 1)]
        for num in candidates:
            if num > target:
                break
            for j in xrange(target - num, 0, -1):
                table[num + j] |= {elt + (num,) for elt in table[j]}
            table[num].add((num,))
        return map(self.divide, map(list, table[target]))

s = Solution()
print(s.combinationSum2([1.15,0.95,1.25,0.25, 0.10], 0.35))