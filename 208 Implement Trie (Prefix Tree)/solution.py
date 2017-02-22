#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Implement a trie with insert, search, and startsWith methods.

# Note:
# You may assume that all inputs are consist of lowercase letters a-z.

class TrieNode(object):

    def __init__(self, char=''):
        self.isWord = False
        self.children = {}
        self.val = char

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        i, track = 0, self.root
        while i < len(word) and word[i] in track.children:
            i, track = i+1, track.children[word[i]]
        while i < len(word):
            track.children[word[i]] = TrieNode(word[i])
            track = track.children[word[i]]
            i += 1
        track.isWord = True

    def search(self, word):
        i, track = 0, self.root
        while i < len(word) and word[i] in track.children:
            i, track = i+1, track.children[word[i]]
        if i == len(word) and track.isWord:
            return True
        return False
        

    def startsWith(self, prefix):
        i, track = 0, self.root
        while i < len(prefix) and prefix[i] in track.children:
            i, track = i+1, track.children[prefix[i]]
        if i == len(prefix):
            return True
        return False
        


if __name__ == "__main__":
    s = Trie()
    s.insert("Trie")
    s.insert("startsWith")
    print(s.search("a"))
    print(s.startsWith("a"))

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)