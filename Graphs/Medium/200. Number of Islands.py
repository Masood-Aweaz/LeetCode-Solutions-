'''********************************************************************************** 
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
**********************************************************************************'''

def BFS(nums, x, y ,l ,m):
    if(x < 0 or y < 0 or x >= l or y >= m or nums[x][y] == "0"):
        return
    nums[x][y] = "0"
    BFS(nums, x, y+1 ,l ,m)
    BFS(nums, x, y-1 ,l ,m)
    BFS(nums, x+1, y ,l ,m)
    BFS(nums, x-1, y ,l ,m)
            
class Solution: 
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count =0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    count+=1
                    BFS(grid,i,j,m,n)
        return count




       
      
        
