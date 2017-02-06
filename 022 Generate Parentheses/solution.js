// Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

// For example, given n = 3, a solution set is:

// [
//   "((()))",
//   "(()())",
//   "(())()",
//   "()(())",
//   "()()()"
// ]

/**
 * @param {number} n
 * @return {string[]}
 */

var generateHelper = function(prefix, queue, n) {
    if (queue === 0 && n === 0)
        return [prefix];
    var res = [];
    if (n !== 0)
        res = res.concat(generateHelper(prefix + '(', queue + 1, n - 1));
    if (queue !== 0)
        res = res.concat(generateHelper(prefix + ')', queue - 1, n));
    return res;
};

var generateParenthesis = function(n) {
    return generateHelper("", 0, n);
};

