// Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

// Note: The solution set must not contain duplicate quadruplets.

// For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

// A solution set is:
// [
//   [-1,  0, 0, 1],
//   [-2, -1, 1, 2],
//   [-2,  0, 0, 2]
// ]

// the idea is the same as 3 sum, and use a recursive approach to do KSum
// TODO: somehow didn't pass due to runtime error, investigate it!

#include <vector>
#include <deque>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        deque<int> nums_deq(nums.begin(), nums.end());
        vector<int> prefix(0);
        return KSum(nums_deq, target, prefix, 4);
    }

    vector<vector<int>> KSum(deque<int> nums, int target, vector<int> prefix, int K) {
        vector<vector<int>> res;
        int n = nums.size();
        if (K == 2) {
            for (int i = 0; i < n; i++) {
                int ind1 = i;
                int ind2 = n - 1;
                while (ind1 < ind2) {
                    int sum = nums[ind1] + nums[ind2];
                    if (sum < target) 
                        ind1++;
                    else if (sum > target)
                        ind2--;
                    else {
                        prefix.push_back(nums[ind1++]);
                        prefix.push_back(nums[ind2--]);
                        res.push_back(prefix);
                        prefix.pop_back();
                        prefix.pop_back();
                        while(ind1 < ind2 && nums[ind1] == nums[ind1 + 1]) ind1++;
                        while(ind1 < ind2 && nums[ind2] == nums[ind2 - 1]) ind2--;
                    }
                }
                i = ind1;
                while (i + 1 < n && nums[i] == nums[i+1]) i++;
            }
        } else {
            for (int i = 0; i < n; i++) {
                int first = nums.front();
                nums.pop_front();  
                prefix.push_back(first);
                vector<vector<int> > subres = KSum(nums, target - first, prefix, K-1);
                prefix.pop_back();
                res.insert(res.end(), subres.begin(), subres.end());

                while ( i + 1 < n && nums[i] == nums[i+1]) {
                    i++;
                }
            }
        }
        return res;
    }
};

int main() {
    auto _a = Solution();
    vector<int> _b = {-493,-482,-482,-456,-427,-405,-392,-385,-351,-269,-259,-251,-235,-235,-202,-201,-194,-189,-187,-186,-180,-177,-175,-156,-150,-147,-140,-122,-112,-112,-105,-98,-49,-38,-35,-34,-18,20,52,53,57,76,124,126,128,132,142,147,157,180,207,227,274,296,311,334,336,337,339,349,354,363,372,378,383,413,431,471,474,481,492};
    auto p = _a.fourSum(_b, 107);
    return 0;
}