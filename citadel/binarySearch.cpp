#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
  int search(vector<int>& nums, int target) {
    if (nums.empty()) {
      return -1;
    }
    unsigned int l = 0, r = nums.size();
    while (l <= r) {
      auto m = l + (r - l) / 2;
      if (nums[m] == target) {
        return m;
      } else if (nums[m] > target) {
        r = m - 1;
      } else {
        l = m + 1;
      }
    }
    return -1;
  }
};

int main() {
  vector<int> nums {1,3,6,12,44,78,79,85,144,233,241};
  Solution a = Solution();
  cout << a.search(nums, 77);
  return 0;
}
