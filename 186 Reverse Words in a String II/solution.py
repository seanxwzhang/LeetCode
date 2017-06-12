#!/usr/bin/env python
# Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

# The input string does not contain leading or trailing spaces and the words are always separated by a single space.

# For example,
# Given s = "the sky is blue",
# return "blue is sky the".

# Could you do it in-place without allocating extra space?

class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        i, j = 0, 0
        while i < len(s):
            while j < len(s) and s[j] != ' ': j += 1
            s[i:j] = s[i:j][::-1]
            i, j = j + 1, j + 1
        s[:] = s[::-1]


s = Solution()
a = ['a', ' ', 'b']
s.reverseWords(a)
print(a)
test(a)
print(a)