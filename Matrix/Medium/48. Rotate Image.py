'''********************************************************************************** 
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
**********************************************************************************'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix)-1
        
        while(l<r):
            
            for i in range(r-l):
                top = l
                bottom = r
                
                #save the topleft element
                temp = matrix[top][l+i]
                
                #move the bottomleft to top left
                matrix[top][l+i] = matrix[bottom-i][l]
                
                #move the bottom right to bottom left
                matrix[bottom-i][l] = matrix[bottom][r-i]
                
                #move the topright to bottom right
                matrix[bottom][r-i] = matrix[top+i][r]
                
                #move the topleft to topright
                matrix[top+i][r] = temp
                
            l+=1
            r-=1
