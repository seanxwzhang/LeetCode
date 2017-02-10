// Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

// The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


// A partially filled sudoku which is valid.

// Note:
// A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        if (board.size() != 9)
            return false;
        if (board[0].size() != 9)
            return false;
        unordered_map<char, bool> rowCheck;
        unordered_map<char, bool> colCheck;
        vector<unordered_map<char, bool>> squareCheck(9);
        // check rows and columns
        for (unsigned i = 0; i < 9; i++) {
            for (unsigned j = 0; j < 9; j++) {
                unsigned indSquare = 3 * (i / 3) + (j / 3);
                char c = board[i][j];
                char cc = board[j][i];
                if ((c != '.' && rowCheck[c]) || (cc != '.' && colCheck[cc]) || (c != '.' && squareCheck[indSquare][c]))
                    return false;
                rowCheck[c] = true;
                colCheck[cc] = true;
                squareCheck[indSquare][c] = true;
            }
            rowCheck.clear();
            colCheck.clear();
        }
        return true;
    }
};