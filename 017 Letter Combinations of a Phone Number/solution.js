// Given a digit string, return all possible letter combinations that the number could represent.

// A mapping of digit to letters (just like on the telephone buttons) is given below.



// Input:Digit string "23"
// Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

// Note:
// Although the above answer is in lexicographical order, your answer could be in any order you want.

/**
 * @param {string} digits
 * @return {string[]}
 */

var mapping = {
    1: ['*'],
    2: ['a','b','c'],
    3: ['d','e','f'],
    4: ['g','h','i'],
    5: ['j','k','l'],
    6: ['m','n','o'],
    7: ['p','q','r','s'],
    8: ['t','u','v'],
    9: ['w','x','y','z'],
    0: []
}

var generateComb = function (digits, prefix) {
    console.log(digits);
    if (digits.length === 0)
        return prefix.length === 0 ? []:[prefix];
    var combs = [];
    var first = digits[0];
    digits.splice(0,1);
    mapping[first].forEach(char => {
        prefix += char;
        combs = combs.concat(generateComb(digits.slice(0), prefix));
        prefix = prefix.slice(0, -1);
    })
    return combs;
}

var letterCombinations = function(digits) {
    return generateComb(digits.toString().split(""), "");
};

console.log(letterCombinations(5231));