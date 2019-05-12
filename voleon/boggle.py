#!/usr/bin/env python3
# boggle game, words are searched vertically, horizontally, and diagnally
from typing import List, Set, Dict
from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' %
              (f.__name__, args, kw, te - ts))
        return result

    return wrap


class Solution1:
    def dfs(self, board: List[List[str]], word_set: Set[str], cur: str, i: int,
            j: int, visited: Set, res: Set[str]):
        if i < 0 or j < 0 or i >= len(board) or j >= len(
                board[0]) or (i, j) in visited:
            return
        cur += board[i][j]
        if cur in word_set and cur not in res:
            res.add(cur)
        visited.add((i, j))
        self.dfs(board, word_set, cur, i + 1, j, visited, res)
        self.dfs(board, word_set, cur, i - 1, j, visited, res)
        self.dfs(board, word_set, cur, i, j + 1, visited, res)
        self.dfs(board, word_set, cur, i, j - 1, visited, res)
        self.dfs(board, word_set, cur, i + 1, j + 1, visited, res)
        self.dfs(board, word_set, cur, i + 1, j - 1, visited, res)
        self.dfs(board, word_set, cur, i - 1, j + 1, visited, res)
        self.dfs(board, word_set, cur, i - 1, j - 1, visited, res)
        visited.remove((i, j))

    @timing
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res, visited, word_set = set(), set(), set(words)
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.dfs(board, word_set, '', i, j, visited, res)
        return list(res)


class Solution2:
    def buildTrie(self, words: List[str]) -> Dict:
        root = {}
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, {})
            node['Terminal'] = True
        return root

    def dfs(self, board: List[List[str]], node: Dict, cur: str, i: int, j: int,
            visited: Set, res: Set[str]):
        if 'Terminal' in node:
            res.add(cur)
            return
        if i < 0 or j < 0 or i >= len(board) or j >= len(
                board[0]) or (i, j) in visited or board[i][j] not in node:
            return
        cur += board[i][j]
        visited.add((i, j))
        self.dfs(board, node[board[i][j]], cur, i + 1, j, visited, res)
        self.dfs(board, node[board[i][j]], cur, i - 1, j, visited, res)
        self.dfs(board, node[board[i][j]], cur, i, j + 1, visited, res)
        self.dfs(board, node[board[i][j]], cur, i, j - 1, visited, res)
        self.dfs(board, node[board[i][j]], cur, i + 1, j + 1, visited, res)
        self.dfs(board, node[board[i][j]], cur, i + 1, j - 1, visited, res)
        self.dfs(board, node[board[i][j]], cur, i - 1, j + 1, visited, res)
        self.dfs(board, node[board[i][j]], cur, i - 1, j - 1, visited, res)
        visited.remove((i, j))

    @timing
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res, visited, root = set(), set(), self.buildTrie(words)
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.dfs(board, root, '', i, j, visited, res)
        return list(res)


board = [[u'o', u'a', u'a', u'n'], [u'e', u't', u'a', u'e'],
         [u'i', u'h', u'k', u'r'], [u'i', u'f', u'l', u'v']]
words = ["oath", "pea", "eat", "rain"]
s1 = Solution1()
s2 = Solution2()
print(s1.findWords(board, words))
print(s2.findWords(board, words))
