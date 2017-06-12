#!/usr/bin/env python

class Solution(object):
    def largestRectangleArea(self, heights):
        heights += 0,
        stack, res = [-1], 0
        for i in xrange(len(heights)):
            while heights[i] < heights[stack[-1]]:
                lb = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, w * lb)
            stack += i,
        heights.pop()
        return res

        