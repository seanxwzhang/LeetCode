# Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

# Example 1:
# Given words = ["bat", "tab", "cat"]
# Return [[0, 1], [1, 0]]
# The palindromes are ["battab", "tabbat"]
# Example 2:
# Given words = ["abcd", "dcba", "lls", "s", "sssll"]
# Return [[0, 1], [1, 0], [3, 2], [2, 4]]
# The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]

# For any palindrom combination, one of the following things should happen (i != j)
# words[i]: 
# words[j]: j0j1j2....jn
# 1. words[j] + words[i][:k] + words[i][k:]:
#     words[i][:k] is a palindrom and words[i][k:] is the reverse of words[j] (k starts at 0)
# 2. words[i][:k] + words[i][k:] + words[j]:
#     words[i][k:] is a palindrom and words[i][:k] is the reverse of words[j] (k ends before len(words[i]) - 1 )

class Solution(object):
    def palindromePairs(self, words):
        rev, res = {word[::-1]: i for i, word in enumerate(words)}, []
        for i, w in enumerate(words):
            for k in xrange(len(w) + 1):
                if w[:k] == w[:k][::-1] and w[k:] in rev and rev[w[k:]] != i:
                    res.append([rev[w[k:]], i])
                if w[k:] == w[k:][::-1] and w[:k] in rev and rev[w[:k]] != i and k < len(w):
                    res.append([i, rev[w[:k]]])
        return res