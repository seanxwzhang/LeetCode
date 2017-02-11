// Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

// The same repeated number may be chosen from C unlimited number of times.

// Note:
// All numbers (including target) will be positive integers.
// The solution set must not contain duplicate combinations.
// For example, given candidate set [2, 3, 6, 7] and target 7, 
// A solution set is: 
// [
//   [7],
//   [2, 2, 3]
// ]

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> res;
        vector<int> cur;
        return backtrack(candidates, cur, res, target, 0);
    }

    vector<vector<int>> backtrack(vector<int>& candidates, vector<int>& cur, vector<vector<int>> &res, int target, int start) {
        if (target == 0)
            res.push_back(cur);
        for (int i = start; i < candidates.size() && candidates[i] <= target; i++) {
            cur.push_back(candidates[i]);
            backtrack(candidates, cur, res, target - candidates[i], i);
            cur.pop_back();
        }
        return res;
    }
};