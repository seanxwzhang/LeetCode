#!/usr/bin/env python

# Given an array of strings, group anagrams together.

# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
# Return:

# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note: All inputs will be in lower-case.

class Solution(object):
    def groupAnagrams(self, strs):
        hashmap, res = {}, []
        for s in strs:
            identifier = str(collections.Counter(list(sorted(s))))
            if identifier in hashmap:
                hashmap[identifier].append(s)
            else:
                hashmap[identifier] = [s]
        for key in hashmap:
            res.append(hashmap[key])
        return res