// Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

// For example:
// Given binary tree [3,9,20,null,null,15,7],
//     3
//    / \
//   9  20
//     /  \
//    15   7
// return its level order traversal as:
// [
//   [3],
//   [9,20],
//   [15,7]
// ]

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        vector<int> tmp;
        deque<TreeNode*> curLevel;
        deque<TreeNode*> nextLevel;
        curLevel.push_back(root);
        TreeNode* track;
        while(!curLevel.empty() || !nextLevel.empty()) {
            if (curLevel.empty()) {
                res.push_back(move(tmp));
                swap(curLevel, nextLevel);
            }
            track = curLevel.front();
            curLevel.pop_front();
            if (track) {
                tmp.push_back(track->val);
                nextLevel.push_back(track->left);
                nextLevel.push_back(track->right);
            }
        }
        return res;
    }
};