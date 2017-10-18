# Given two binary strings, return their sum (also a binary string).

# For example,
# a = "11"
# b = "1"
# Return "100".

class Solution(object):
    def addBinary(self, a, b):
        c = int(a, 2) + int(b, 2)
        return '{0:b}'.format(c)