#!/usr/bin/env python

# Write a program to solve a Sudoku puzzle by filling the empty cells.

# Empty cells are indicated by the character '.'.

# You may assume that there will be only one unique solution.


# A sudoku puzzle...
# 13974865.
# 7........
# .2.1.9...
# ..7...24.
# .64.1.59.
# .98...3..
# ...8.3.2.
# ........6
# ...2759..
# ...and its solution numbers marked in red.

# this is a brutal force solution, works but too slow
class Solution(object):
    def solveSudoku(self, board):
        self.helper(board)

    def helper(self, board):
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c == '.':
                    row_taken = set([board[i][ii] for ii in xrange(9)])
                    col_taken = set([board[jj][j] for jj in xrange(9)])
                    sq_taken = set([board[rr][cc] for rr in xrange(i/3*3, i/3*3+3) for cc in xrange(j/3*3, j/3*3+3)])
                    taken = row_taken | col_taken | sq_taken
                    ms = [str(x) for x in xrange(1, 10) if str(x) not in taken] # possible moves
                    for move in ms:
                        board[i][j] = move
                        if self.helper(board): return True # if it works
                    board[i][j] = '.'
                    return False # if no possible moves work, return false
        return True # if no empty slots, return True

s = Solution()
board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
board = [list(row) for row in board]
s.solveSudoku(board)
print(board)