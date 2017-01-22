# Find the largest palindrome made from the product of two n-digit numbers.
#
# Since the result could be very large, you should return the largest palindrome mod 1337.
#
# Example:
#
# Input: 2
#
# Output: 987
#
# Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
#
# Note:
#
# The range of n is [1,8].

# Approach: Find the largest possible product from two n-digit number and start checking towards small numbers, return the first palindrome
# Also check if the number can be decomposed into two numbers
# Python may not be fast enough
# TODO: write a C++ version
class Solution(object):
    def nextPalindrome(self, n):
        l = len(str(n))
        left = int(str(n)[:int(l / 2)])
        right = int(str(n)[int((l + 1) / 2):])
        if int(str(left)[::-1]) < right:
            return int(str(left) + (str(n)[int(l / 2)] if l % 2 else "") + str(left)[::-1])
        else:
            return int(str(left - 1) + (str(n)[int(l / 2)] if l % 2 else "") + str(left - 1)[::-1])

    def largestPalindrome(self, n):
        if n == 1:
            return 9
        maxn = 10 ** (2 * n) - 2 * (10 ** n) + 1
        maxi = 10 ** n - 1
        while True:
            maxn = self.nextPalindrome(maxn)
            gap = -1 if maxn % 2 else -2
            for i in range(maxi, int(maxn ** 0.5), gap):
                if maxn % i == 0 and maxn / i <= maxi:
                    return maxn % 1337
        return 1

if __name__ == "__main__":
    s = Solution()
    print(s.largestPalindrome(1))