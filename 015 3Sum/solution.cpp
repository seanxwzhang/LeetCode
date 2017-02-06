// # Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

// # Note: The solution set must not contain duplicate triplets.

// # For example, given array S = [-1, 0, 1, 2, -1, -4],

// # A solution set is:
// # [
// #   [-1, 0, 1],
// #   [-1, -1, 2]
// # ]


#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<vector<int > > threeSum(vector<int>& nums) {
      vector<vector<int > > res;
      sort(nums.begin(), nums.end());
      for (int i = 0; i + 2 < nums.size(); i++) {
        int target = nums[i];
        int ind1 = i + 1;
        int ind2 = nums.size() - 1;
        while (ind1 < ind2) {
          if (nums[ind1] + nums[ind2] < -target) {
            ind1++;
          } else if (nums[ind1] + nums[ind2] > -target) {
            ind2--;
          } else {
            vector<int> tmp = {target, nums[ind1], nums[ind2]};
            res.push_back(tmp);
            while(ind1 < ind2 && nums[ind1] == nums[ind1 + 1])  ind1++;
            while(ind1 < ind2 && nums[ind2] == nums[ind2 - 1])  ind2--;
            ind1++;
            ind2--;
          }
        }
        while (i + 1 < nums.size() && nums[i + 1] == nums[i]) 
            i++;
      }
      return res;
    }
};
