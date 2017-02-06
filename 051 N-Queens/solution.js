// The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



// Given an integer n, return all distinct solutions to the n-queens puzzle.

// Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

// For example,
// There exist two distinct solutions to the 4-queens puzzle:

// [
//  [".Q..",  // Solution 1
//   "...Q",
//   "Q...",
//   "..Q."],

//  ["..Q.",  // Solution 2
//   "Q...",
//   "...Q",
//   ".Q.."]
// ]

/**
 * @param {number} n
 * @return {string[][]}
 */


var solveNQueens = function(n) {
    var res = [];
    var columnAvalability = [];
    var leftDiagnal = [];
    var rightDiagnal = [];

    var putQueen = function(n, row, sofar) {
        for (let col = 0; col < n; col ++) {
            if (!columnAvalability[col] && !leftDiagnal[col + row] && !rightDiagnal[row - col + (n - 1)]) {
                columnAvalability[col] = 1;
                leftDiagnal[col + row] = 1;
                rightDiagnal[row - col + n - 1] = 1;
                sofar.push(".".repeat(col) + 'Q' + ".".repeat(n - col - 1));
                if (row < n - 1)
                    putQueen(n, row + 1, sofar);
                else
                    res.push(sofar.slice(0));
                sofar.pop();
                rightDiagnal[row - col + n - 1] = 0;
                leftDiagnal[col + row] = 0;
                columnAvalability[col] = 0;
            }
        }
    };

    for (let i =0; i < n; i++) {
        columnAvalability.push(0);
    }
    for (let i = 0; i < 2*n - 1; i++) {
        leftDiagnal.push(0);
        rightDiagnal.push(0);
    }
    putQueen(n, 0, []);
    return res;
};

/**
 * @param {max_row} n
 * @param {current_row} row
 * @param {current_solution} sofar 
 */


console.log(solveNQueens(1));
