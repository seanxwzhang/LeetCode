// Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

//     For example, given array S = {-1 2 1 -4}, and target = 1.

//     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int sofar = INT_MAX;
        for (int i = 0; i < nums.size(); i++) {
            int cur = -nums[i];
            int j = i+1, k = nums.size() - 1;
            while(j < k) {
                int sum = nums[j] + nums[k];
                if (sum < cur)  
                    j++;
                else if (sum > cur)
                    k--;
                sofar = min(sofar, sum - cur);
                if (sofar == 0) return sofar;
                while(j < k && nums[j] == nums[j+1]) j++;
                while(j < k && nums[k] == nums[k-1]) k--;
            }
            while(i < nums.size() - 1 && nums[i] == nums[i+1]) i++;
        }
        return sofar;
    }
};