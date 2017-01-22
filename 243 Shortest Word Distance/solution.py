#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
#
# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.
#
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
#
# This solution is not ideal, could drop the complexity down to O(n), space to O(1)
import sys
import bisect
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        dic = {}
        dist = sys.maxsize
        for idx, word in enumerate(words):
            if dic.has_key(word):
                dic[word].append(idx)
            else:
                dic[word] = [idx]
        for id1 in dic[word1]: # find the closest
            insertion = bisect.bisect_left(dic[word2], id1)
            closest = dic[word2][insertion] if insertion < len(dic[word2]) and abs(dic[word2][insertion] - id1) < abs(dic[word2][insertion - 1] - id1) else dic[word2][insertion - 1]
            dist = min(dist, abs(id1 - closest))
        return dist


if __name__ == "__main__":
    words = ["this","is","a","long","sentence","is","fun","day","today","sunny","weather","is","a","day","tuesday","this","sentence","run","running","rainy"]
    word1 = "sentence"
    word2 = "a"
    s = Solution()
    print(s.shortestDistance(words, word1, word2))

