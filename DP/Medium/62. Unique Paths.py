
'''********************************************************************************** 
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
**********************************************************************************'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def solve(i,j):
            if i == m-1 or j == n-1:
                return 1
            
            if dp[i][j]:
                return dp[i][j]
            
            dp[i][j]=solve(i+1,j)+solve(i,j+1)
            return dp[i][j]
        
        
        dp = [[0 for i in range(n)]for j in range(m)]
        #print(dp)
        return solve(0,0)
        
        
        
    
    
       
