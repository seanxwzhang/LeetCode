# Given a 2D board and a list of words from the dictionary, find all words in the board.

# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

# For example,
# Given words = ["oath","pea","eat","rain"] and board =

# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# Return ["eat","oath"].
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.



class Solution(object):
    def getPrefix(self, words):
        res = set()
        for w in words:
            for i in xrange(1, len(w) + 1):
                res.add(w[:i])
        return res

    def getTrie(self, words):
        root = {}
        for word in words:
            node = root
            for c in word:
                node = node.setdefault(c, {})
            node[None] = True
        return root

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]:
            return []
        self.board = board
        trie = self.getTrie(words)
        self.visited, res = [[False for _ in range(len(board[0]))] for _ in range(len(board))], set()
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                    self.dfs(i, j, '', trie, res)
        return list(res)

    def dfs(self, i, j, cur, trie, res):
        if None in trie:
            res.add(cur)
        if i < 0 or j < 0 or i >= len(self.board) or j >= len(self.board[0]) or self.visited[i][j] or self.board[i][j] not in trie:
            return
        cur += self.board[i][j]
        self.visited[i][j], newTrie = True, trie[self.board[i][j]]
        self.dfs(i - 1, j, cur, newTrie, res)
        self.dfs(i, j - 1, cur, newTrie, res)
        self.dfs(i + 1, j, cur, newTrie, res)
        self.dfs(i, j + 1, cur, newTrie, res)
        self.visited[i][j] = False

board = [[u'o', u'a', u'a', u'n'], [u'e', u't', u'a', u'e'], [u'i', u'h', u'k', u'r'], [u'i', u'f', u'l', u'v']]
words = ["oath","pea","eat","rain"]
s = Solution()
print(s.findWords(board, words))
        


        
