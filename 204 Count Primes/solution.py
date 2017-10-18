# Description:

# Count the number of prime numbers less than a non-negative number, n.

# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.
import math

class Solution(object):
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [True] * n
        primes[0], primes[1] = False, False
        for i in xrange(2, int(math.sqrt(n)) + 1):
            if primes[i]:
                primes[i**2:n:i] = [False]*len(primes[i**2:n:i])
        return sum(primes)
