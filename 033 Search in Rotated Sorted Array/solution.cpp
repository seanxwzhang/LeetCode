// Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

// (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

// You are given a target value to search. If found in the array return its index, otherwise return -1.

// You may assume no duplicate exists in the array.
#include <vector>
#include <cstdint>
#include <iostream>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (nums.empty()) return -1;
        int l = 0, r = nums.size() - 1, mid = 0;
        // find the largest value
        while (l < r) {
            mid = (l + r) / 2;
            if (nums[l] > nums[mid])    r = mid;
            else if (nums[l] == nums[mid]) l = mid+1;
            else    l = mid;
        }
        mid = l;
        // binary search
        if (target >= nums[0])
            return binarySearch(nums, 0, mid, target);
        return binarySearch(nums, mid, nums.size() - 1, target);
    };

    // increasing
    int binarySearch(vector<int>& nums, int l, int r, int target) { 
        int mid = 0;
        while(l < r) {
            mid = (l + r) / 2;
            if (nums[mid] < target)
                l++;
            else if (nums[mid] > target)
                r--;
            else
                return mid;
        }
        if (nums[r] == target)
            return r;
        return -1;
    }
};

int main() {
    vector<int> r = {4,5,6,7,0,1,2};
    auto s = Solution();
    cout << s.search(r, 0) << endl;
}