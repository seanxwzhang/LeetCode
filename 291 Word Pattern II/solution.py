# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

# Examples:
# pattern = "abab", str = "redblueredblue" should return true.
# pattern = "aaaa", str = "asdasdasdasd" should return true.
# pattern = "aabb", str = "xyzabcxzyabc" should return false.
# Notes:
# You may assume both pattern and str contains only lowercase letters.


class Solution(object):
    def __init__(self):
        self.ctostr, self.strtoc = {}, {}

    def wordPatternMatch(self, pattern, str):
        return self.findPatternMatch(pattern, str, 0, 0)

    def findPatternMatch(self, pattern, str, ind, strInd):
        if (ind == len(pattern) and strInd != len(str)) or (ind != len(pattern) and strInd == len(str)): return False
        if ind == len(pattern) and strInd == len(str): return True
        if pattern[ind] not in self.ctostr: # if we haven't encounter this new char before
            # try every mapping possible
            for length in xrange(1, len(str) - strInd + 1):
                candidate = str[strInd:(strInd + length)]
                if candidate in self.strtoc:
                    continue
                self.ctostr[pattern[ind]] = candidate
                self.strtoc[candidate] = pattern[ind]
                if self.findPatternMatch(pattern, str, ind + 1, strInd + length):
                    return True
                self.ctostr.pop(pattern[ind])
                self.strtoc.pop(candidate)
            return False
        else: # we have encountered this char before
            assumption = self.ctostr[pattern[ind]]
            if strInd + len(assumption) > len(str) or str[strInd:(strInd + len(assumption))] != assumption:
                return False
            return self.findPatternMatch(pattern, str, ind + 1, strInd + len(assumption))

if __name__ == "__main__":
    s = Solution()
    print(s.wordPatternMatch("ababacdefg", "redblueredbluereddasds"))
