// Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

// The approach is to maintain a queue

/**
 * @param {string} s
 * @return {boolean}
 */

var mapping = {
    '(': ')',
    '[': ']',
    '{': '}'
};
var isValid = function(s) {
    var queue = [];
    var str = s.split("");
    for (var i = 0; i < str.length; i++) {
        if (queue.length === 0 || str[i] in mapping)
            queue.push(str[i]);
        else if (mapping[queue[queue.length - 1]] == str[i])
            queue.pop();
        else
            return false;
    }
    return (queue.length === 0);
};