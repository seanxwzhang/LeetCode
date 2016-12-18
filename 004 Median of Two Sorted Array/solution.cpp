/*
    There are two sorted arrays nums1 and nums2 of size m and n respectively.
    Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
*/

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size(), n = nums2.size();
        if (m > n) { // make sure nums1 is always smaller than nums2
            nums1.swap(nums2);
            swap(m, n);
        }
        if (m == 0) {
            if (n % 2)
                return nums2[n / 2 + 1];
            else
                return nums2[n / 2];
        }
        int i, j, left = -1, right = m - 1; 
        while (left <= right) {
            i = (left + right) / 2;
            j = (n + m - 3) / 2 - i;
            if ( i >= 0 && nums1[i] > nums2[j + 1]) {
                right = i - 1;
            } else if (j >= 0 && nums2[j] > nums1[i + 1]) {
                left = i + 1;
            } else { // found the i
                int left_max, right_min;
                if (i < 0) 
                    left_max = nums2[j];
                else if (j < 0)
                    left_max = nums1[i];
                else   
                    left_max = max(nums2[j], nums1[i]);
                
                if ((m + n) % 2)
                    return left_max;

                if (i == m - 1)
                    right_min = nums2[j+1];
                else if (j == n - 1)
                    right_min = nums1[i+1];
                else
                    right_min = min(nums2[j+1], nums1[i+1]);
                
                return (left_max + right_min) / 2;
            }
        }
    }
};