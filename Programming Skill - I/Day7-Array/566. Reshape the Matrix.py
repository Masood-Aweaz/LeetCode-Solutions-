'''********************************************************************************** 
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.


Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
**********************************************************************************'''

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        if n*m == r*c:
            #new_mat = [[0 for _ in range(c)]]*r
            #print(new_mat)
            col = 0
            row = []
            new_mat = []
            for i in mat:
                for j in i:
                    row.append(j)
                    col += 1
                    if col == c:
                        col = 0
                        new_mat.append(row)
                        row = []
            return new_mat
        return mat
                        
            
                    
