#!/usr/bin/env python

# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

# Examples:
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

class Solution(object):
    def wordPattern(self, pattern, str):
        ctostr, strtoc, strarr = {}, {}, str.split(' ')
        if len(pattern) != len(strarr):
            return False
        for char, word in zip(pattern, strarr):
            if char not in ctostr and word not in strtoc:
                ctostr[char] = word
                strtoc[word] = char
            elif char in ctostr and word in strtoc and ctostr[char] == word and strtoc[word] == char:
                continue
            else:
                return False
        return True
