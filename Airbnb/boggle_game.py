# Boggle game, use trie to speed up search


def getTrie(words):
    root = {}
    for w in words:
        node = root
        for char in w:
            node = node.setdefault(char, {})
        node[None] = None
    return root


def boggleGame(board, words):
    trie, res, visited = getTrie(words), set(), set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(board, '', i, j, trie, visited, res)
    return list(res)


def dfs(board, cur, i, j, node, visited, res):
    if None in node:
        res.add(cur)
    if i < 0 or i < 0 or i >= len(board) or j >= len(
            board[0]) or (i, j) in visited:
        return
    if board[i][j] not in node:
        return
    visited.add((i, j))
    cur += board[i][j]
    dfs(board, cur, i - 1, j, node[board[i][j]], visited, res)
    dfs(board, cur, i + 1, j, node[board[i][j]], visited, res)
    dfs(board, cur, i, j + 1, node[board[i][j]], visited, res)
    dfs(board, cur, i, j - 1, node[board[i][j]], visited, res)
    visited.remove((i, j))
    return res


board = [[u'o', u'a', u'a', u'n'], [u'e', u't', u'a', u'e'],
         [u'i', u'h', u'k', u'r'], [u'i', u'f', u'l', u'v']]
words = ["oath", "pea", "eat", "rain"]
print(boggleGame(board, words))
