// Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


// Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


// The largest rectangle is shown in the shaded area, which has area = 10 unit.

// For example,
// Given heights = [2,1,5,6,2,3],
// return 10.

// O(n) solution using stack
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int> indices;
        int n = heights.size(), largest = 0, i = 0;
        while (i < n) {
            if (indices.empty() || heights[indices.top()] <= heights[i]) {
                indices.push(i++);
            } else {
                int cur = indices.top();
                indices.pop();
                int side = indices.empty() ? i : (i - indices.top() - 1);
                largest = max(largest, heights[cur] * side);
            }
        }
        while(!indices.empty()) {
            int cur = indices.top();
            indices.pop();
            int side = indices.empty() ? n : (n - indices.top() - 1);
            largest = max(largest, heights[cur] * side);
        }
        return largest;
    }
};