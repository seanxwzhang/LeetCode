#include <vector>
#include <iostream>
#include <unordered_map>
#include <initializer_list>

using namespace std;

class Solution {
public:
  vector<vector<int> > threeSum(vector<int>& nums) {
    vector<vector<int>> res;
    sort(nums.begin(), nums.end());
    for (int i = 0; i + 2 < nums.size(); i++) {
      int target = -nums[i];
      int i1 = i + 1, i2 = nums.size() - 1;
      while (i1 < i2) {
        auto sum_2 = nums[i1] + nums[i2];
        if (sum_2 > target) {
          i2--;
        } else if (sum_2 < target) {
          i1++;
        } else {
          // res.emplace_back(initializer_list<int>({-target, nums[i1], nums[i2]}));
          vector<int> tmp = {target, nums[i1], nums[i2]};
          res.push_back(move(tmp));
          while(i1 < i2 && nums[i1] == nums[i1+1])  i1++;
          while(i1 < i2 && nums[i2] == nums[i2-1])  i2--;
          i1++;
          i2--;
        }
      }
      while (i + 1 < nums.size() && nums[i + 1] == nums[i]) {
        i++;
      }
    }
    return res;
  }
};
