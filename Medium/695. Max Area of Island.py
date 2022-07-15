
'''********************************************************************************** 
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
**********************************************************************************'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        def area(row,col):
            if not (0<=row<len(grid) and 0<=col<len(grid[0]) and (row,col) not in visited and grid[row][col]!=0):
                return 0
            visited.add((row,col))
            return (1+area(row+1,col)+area(row-1,col)+area(row,col+1)+area(row,col-1)) #4 neighbours
        
        return max(area(row,col) for row in range(len(grid)) for col in range(len(grid[0])))
