// Follow up for N-Queens problem.

// Now, instead outputting board configurations, return the total number of distinct solutions.

var totalNQueens = function(n) {
    var res = 0;
    var columnAvalability = [];
    var leftDiagnal = [];
    var rightDiagnal = [];

    var putQueen = function(n, row) {
        for (let col = 0; col < n; col ++) {
            if (!columnAvalability[col] && !leftDiagnal[col + row] && !rightDiagnal[row - col + (n - 1)]) {
                columnAvalability[col] = 1;
                leftDiagnal[col + row] = 1;
                rightDiagnal[row - col + n - 1] = 1;
                // sofar.push(".".repeat(col) + 'Q' + ".".repeat(n - col - 1));
                if (row < n - 1)
                    putQueen(n, row + 1);
                else
                    res++;
                // sofar.pop();
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
    putQueen(n, 0);
    return res;
};