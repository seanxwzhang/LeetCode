// Given a binary tree, return the inorder traversal of its nodes' values.

// For example:
// Given binary tree [1,null,2,3],
//    1
//     \
//      2
//     /
//    3
// return [1,3,2].

// Note: Recursive solution is trivial, could you do it iteratively?

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var inorderTraversal = function(root) {
    var recursive = function(_root, sofar) {
        if (_root.left)
            recursive(_root.left, sofar);
        sofar.push(_root.val);
        if (_root.right)
            recursive(_root.right, sofar);
    };
    var iterative = function(_root) {
        var res = [];
        var stack = [];
        while(_root || stack.length > 0) {
            while(_root) {
                stack.push(_root);
                _root = _root.left;
            }
            _root = stack.pop();
            res.push(_root.val);
            _root = _root.right;
        }
        return res;
    };
    // recursive way
    // var res = [];
    // recursive(root, res);
    // return res;
    // iterative way
    return iterative(root);
};
