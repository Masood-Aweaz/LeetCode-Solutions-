'''********************************************************************************** 
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.



Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
**********************************************************************************'''

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        #print(n,m)
        res=[]
        rev_mat = mat[::-1]
        #print(rev_mat)
        for i in range(n):
            for j in range(m):
                if i==j:
                    res.append(mat[i][j])
                    res.append(rev_mat[i][j])
        if m%2==1 and n%2==1:
            return sum(res)-mat[n//2][m//2]
        else:
            return sum(res)
        
