#!/usr/bin/env python

# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# For "(()", the longest valid parentheses substring is "()", which has length = 2.

# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

class Solution(object):
    def longestValidParentheses(self, s):
        longest, stack, i = 0, [], 0
        for i in xrange(len(s)):
            if s[i] == '(':
                stack += i,
            elif s[i] == ')' and stack and s[stack[-1]] == '(':
                stack.pop()
                longest = max(longest, i - (stack[-1] if stack else -1))
            else:
                stack += i,
        return longest

s = Solution()
print(s.longestValidParentheses("()"))