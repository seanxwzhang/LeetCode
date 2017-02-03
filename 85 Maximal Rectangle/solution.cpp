// Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

// For example, given the following matrix:

// 1 0 1 0 0
// 1 0 1 1 1
// 1 1 1 1 1
// 1 0 0 1 0
// Return 6.

// Approach, this solution is built on top of Largest Rectangle in Histogram

class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.empty() || matrix[0].empty())
            return 0;
        int m = matrix.size(), n = matrix[0].size(), largest = 0;
        vector<int> row(n, 0);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                row[j] = matrix[i][j] == '0' ? 0 : row[j] + 1;
            }
            largest = max(largest, largestRectangleArea(row));
        }
        return largest;
    }

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