// # Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

// # Note: The solution set must not contain duplicate triplets.

// # For example, given array S = [-1, 0, 1, 2, -1, -4],

// # A solution set is:
// # [
// #   [-1, 0, 1],
// #   [-1, -1, 2]
// # ]

// This solution is hard to reason about duplicate values
// class Solution {
// public:
//     vector<vector<int>> threeSum(vector<int>& nums) {
//         sort(nums.begin(), nums.end());
//         vector<vector<int>> res;
//         int n = nums.size();
//         for (int i = 0; i < n; i++) {
//             if (i == 0 || nums[i] != nums[i - 1]) {
//                 auto tmp = twoSum(nums, i, -nums[i]);
//                 res.insert(res.begin(), tmp.begin(), tmp.end());
//             }
//         }
//         return res;
//     }

//     vector<vector<int>> twoSum(vector<int>&nums, int start, int target) {
//         unordered_map<int, int> hashmap;
//         vector<vector<int>> res;
//         int n = nums.size();
//         for (int i = start + 1; i < n; i++) {
//             if (hashmap.count(target - nums[i]) && (!hashmap.count(nums[i]) || hashmap[nums[i]]) {
//                 vector<int> pair = {-target, nums[i], target - nums[i]};
//                 res.push_back(move(pair));
//             } 
//             hashmap[nums[i]] = i;
//         }
//         return res;
//     }
// };