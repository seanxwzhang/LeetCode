#!/usr/bin/env python

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# 11110
# 11010
# 11000
# 00000
# Answer: 1

# Example 2:

# 11000
# 11000
# 00100
# 00011
# Answer: 3

class Solution(object):
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        visited = [[0 for i in j] for j in grid]
        res = 0
        for row in xrange(len(grid)):
            for col in xrange(len(grid[0])):
                if grid[row][col] == '1' and not visited[row][col]:
                    res += 1
                    self.explore(grid, visited, row, col)
        return res
    
    def explore(self, grid, visited, row, col):
        print("exploring" + str(row) + ', ' + str(col))
        visited[row][col] = 1
        if row > 0 and grid[row - 1][col] == '1' and not visited[row - 1][col]: self.explore(grid, visited, row - 1, col)
        if row < len(grid) - 1 and grid[row + 1][col] == '1' and not visited[row + 1][col]: self.explore(grid, visited, row + 1, col)
        if col > 0 and grid[row][col - 1] == '1' and not visited[row][col - 1]: self.explore(grid, visited, row, col - 1)
        if col < len(grid[0]) - 1 and grid[row][col + 1] == '1' and not visited[row][col + 1]: self.explore(grid, visited, row, col + 1)
        
if __name__ == "__main__":
    testcase = ["11000","11000","00100","00011"]
    s = Solution()
    print(s.numIslands(testcase))