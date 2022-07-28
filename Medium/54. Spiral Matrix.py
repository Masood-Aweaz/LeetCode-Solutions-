'''********************************************************************************** 
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
**********************************************************************************'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left , right = 0, len(matrix[0])
        top , bottom = 0, len(matrix)
        res=[]
        
        while left<right and top<bottom:
            #moving the top row from left to right
            for i in range(left,right):
                res.append(matrix[top][i])
            top+=1
                
            #moving the right column from top to down
            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            right-=1
                
            if not (left<right and top<bottom):
                break
                
            #moving the bottom row from right to left
            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])
            bottom-=1
                
            #moving the left column from bottom to top
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
            left+=1
                
        return res
