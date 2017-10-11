# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

# Note:

# The length of both num1 and num2 is < 110.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution(object):
    def multiply(self, num1, num2):
        res = [0] * (len(num1) + len(num2))
        for i, vi in enumerate(num1):
            for j, vj in enumerate(num2):
                mul = int(vi) * int(vj)
                res[i+j+1] += mul % 10
                res[i+j] += mul / 10
        for i in xrange(len(res) - 1, 0, -1):
            res[i - 1] += res[i] / 10
            res[i] %= 10
        ans = ''.join(map(str, res)).lstrip('0')
        return ans if ans else '0'

s = Solution()
print(s.multiply('0','0'))