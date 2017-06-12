# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


# A partially filled sudoku which is valid.

# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.


class Solution(object):
    def isValidSudoku(self, board):
        return 1 == max(collections.Counter(
            x
            for i, row in enumerate(board)
            for j, char in enumerate(row)
            if char != '.'
            for x in ((i, char), (char, j), (i/3, j/3, char))
        ).values() + [1])

s = Solution()
a = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]

