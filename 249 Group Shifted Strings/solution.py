#!/usr/bin/env python
# Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

# For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
# A solution is:

# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]


class Solution(object):
    def transform(self, immutablestring):
        string = list(immutablestring)
        if not string:
            return string
        shift = ord(string[0]) - ord('a')
        for i in xrange(len(string)):
            string[i] = chr(ord('a') + (ord(string[i]) - ord('a') - shift) % 26)
        return ''.join(string)

    def groupStrings(self, strings):
        hashmap, res = {}, []
        for string in strings:
            trans = self.transform(string)
            if trans in hashmap:
                hashmap[trans].append(string)
            else:
                hashmap[trans] = [string]
        for key in hashmap:
            res.append(hashmap[key])
        return res