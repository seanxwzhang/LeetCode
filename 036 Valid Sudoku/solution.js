// Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

// The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


// A partially filled sudoku which is valid.

// Note:
// A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.


/**
 * @param {character[][]} board
 * @return {boolean}
 */

var isValidSudoku = function(board) {
    var checkRow = function(row) {
        let mapping = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0};
        for (let i = 0; i < row.length; i++) {
            if (row[i] != '.') {
                if (mapping[row[i]])
                    return false;
                mapping[row[i]] = 1;
            }
        }
        return true;
    }
};