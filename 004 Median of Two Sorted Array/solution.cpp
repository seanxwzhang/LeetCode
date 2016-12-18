/*
    There are two sorted arrays nums1 and nums2 of size m and n respectively.
    Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
*/

#include <vector>
#include <cmath>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size(), n = nums2.size();
        if (m > n) { // make sure nums1 is always smaller than nums2 and m <= n
            nums1.swap(nums2);
            swap(m, n);
        }
        if (n == 0) {
            if (n % 2)
                return nums2[m / 2 + 1];
            else
                return nums2[m / 2];
        }
        int i, j, left = 0, right = m;
        while (left <= right) {
            i = (left + right) / 2;
            j = (n + m + 1) / 2 - i;
            if ( i > 0 && nums1[i - 1] > nums2[j]) {
                right = i - 1;
            } else if (i < m && nums2[j - 1] > nums1[i]) {
                left = i + 1;
            } else { // found the i
                int left_max, right_min;
                if (i == 0)
                    left_max = nums2[j - 1];
                else if (j == 0)
                    left_max = nums1[i - 1];
                else
                    left_max = max(nums2[j - 1], nums1[i - 1]);

                if ((m + n) % 2)
                    return left_max;

                if (i == m )
                    right_min = nums2[j];
                else if (j == n)
                    right_min = nums1[i];
                else
                    right_min = min(nums2[j], nums1[i]);

                return double(left_max + right_min) / 2;
            }
        }
        return 0;
    }
};

int main() {
    vector<int> a = {1, 2};
    vector<int> b = {3, 4};
    Solution s;
    double ans = s.findMedianSortedArrays(a, b);
    cout << ans << endl;
    return 0;
}