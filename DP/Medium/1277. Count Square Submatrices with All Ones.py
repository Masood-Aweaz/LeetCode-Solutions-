'''********************************************************************************** 
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
**********************************************************************************'''

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        r = len(matrix)
        c = len(matrix[0])
        
        dp = [[0]*c for i in range(r) ]
        print(dp)
        
        for i in range(r):
            for j in range(c):
                if i==0 or j==0: #fill firts row and col in dp as matrix 
                    dp[i][j] = matrix[i][j]
                else:
                    if matrix[i][j]==0:
                        dp[i][j]=0
                    else:
                        dp[i][j] = 1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        x = [dp[i][j] for i in range(r) for j in range(c)]
        return sum(x)
