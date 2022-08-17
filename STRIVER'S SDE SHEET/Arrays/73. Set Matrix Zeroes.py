class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lst=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    lst.append([i,j])
        #print(lst)

        for i in lst:
            row = i[0]
            col = i[1]
            for c in range(len(matrix[0])):
                matrix[row][c]=0
            for r in range(len(matrix)):
                matrix[r][col]=0
