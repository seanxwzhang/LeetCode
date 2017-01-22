#!/usr/bin/env python
# A tail-recursive solution, O(n) time
class RSolution(object):
    longest = 0

    def helper(self, current, paths):
        # current stores the lengths of the current candidates as a list
        if not paths:
            return self.longest
        else:
            path = paths.pop()
            current = current[:-(len(current) - path.count("\t")) or None]
            if "." in path:
                self.longest = max(self.longest, sum(current) + len(path)- len(current) + (1 if len(current) > 0 else 0))
            else:
                current.append(len(path) - path.count("\t") + (1 if len(current) > 0 else 0))
            return self.helper(current, paths)

    def lengthLongestPath(self, input):
        paths = input.split('\n')
        paths.reverse()
        return self.helper(list(), paths)

# A iterative solution, O(n) time, O(1) space
class Solution(object):
    def lengthLongestPath(self, input):
        paths = input.splitlines()
        current = []
        longest = 0
        for path in paths:
            name = path.lstrip("\t")
            depth = len(path) - len(name)
            current = current[:-(len(current) - depth) or None]
            if "." in path:
                longest = max(longest, sum(current) + len(name) + (1 if len(current) > 0 else 0))
            else:
                current.append(len(name) + (1 if len(current) > 0 else 0))
        return longest


if __name__ == "__main__":
    s = Solution()
    testpath = "dir\n    file.txt"
    print(s.lengthLongestPath(testpath))
