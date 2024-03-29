'''********************************************************************************** 
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

 

Example 1:


Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
**********************************************************************************'''

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def sort(mat,row,col,m,n):
            values = []
            r = row
            c = col
            
            while(r<m and c<n):
                values.append(mat[r][c])
                r+=1
                c+=1
            
            values.sort()
            ind = 0
            while(row<m and col<n):
                mat[row][col]=values[ind]
                ind+=1
                row+=1
                col+=1
                
                
        m = len(mat)
        n = len(mat[0])
        
        #for row 0
        for c in range(n):
            sort(mat,0,c,m,n)
            
        #for col 0
        for r in range(m):
            sort(mat,r,0,m,n)
        
        return mat
    
    
    
        
                
