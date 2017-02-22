#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 题目不太放水，让我实现一个网页上的自动补全的功能。就是你输入prefix，然后下面会返回从这个前缀开始的所有单词。其实就是写一个trie就行了。然后这个返回的结果要根据用户的点击次数来sort。因为当时7月，也就是4个月前，当时我刷题还没刷太熟。所以最后只写到了128 Implement Trie (Prefix Tree) ，然后返回从这个前缀开始的所有单词没写出来。其实从那里接一个dfs就行了

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
            track.children[word[i]] = TrieNode(track.val + word[i])
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
    
    def allstartsWith(self, prefix):
        i, track, res = 0, self.root, []
        while i < len(prefix) and prefix[i] in track.children:
            i, track = i+1, track.children[prefix[i]]
        if i == len(prefix): # starts breadth first search and sort them
            bfsq = []
            while track or bfsq:
                for char in track.children:
                    bfsq.append(track.children[char])
                    if track.children[char].isWord:
                        res.append(track.children[char].val)
                track = None if not bfsq else bfsq.pop(0)
        return res

if __name__ == "__main__":
    s = Trie()
    s.insert("Trie")
    s.insert("Trie is good")
    s.insert("Trid is bad")
    s.insert("good")
    print(s.allstartsWith("Trid"))