// Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

// For example:
// Given binary tree [3,9,20,null,null,15,7],
//     3
//    / \
//   9  20
//     /  \
//    15   7
// return its bottom-up level order traversal as:
// [
//   [15,7],
//   [9,20],
//   [3]
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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        deque<vector<int>> tmp;
        vector<vector<int>> res;
        vector<int> cur;
        deque<TreeNode*> queue;
        queue.push_back(root);
        queue.push_back(nullptr);
        TreeNode* track;
        while(!queue.empty()) {
            track = queue.front();
            queue.pop_front();
            if (track == nullptr) {
                if (!cur.empty())   tmp.push_front(move(cur));
            } else {
                cur.push_back(track->val);
                if (track->left) queue.push_back(track->left);
                if (track->right) queue.push_back(track->right);
                if (queue.front() == nullptr) queue.push_back(nullptr);
            }
        }
        res.assign(tmp.begin(), tmp.end());
        return res;
    }
};