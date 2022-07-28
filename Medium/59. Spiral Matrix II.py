'''********************************************************************************** 
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
**********************************************************************************'''

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        #res=[[0]*n]*n
        res=[row[:] for row in [[0]*n]*n]
        left , right = 0,n
        top, bottom = 0,n
        print(res)
        c=1
        while left<right and top<bottom:
            for i in range(left,right):
                print(res[top][i])
                res[top][i]=c
                c+=1
            top+=1
            
            for i in range(top,bottom):
                res[i][right-1]=c
                c+=1
            right-=1
            
            if not(left<right and top<bottom):
                break
                
            for i in range(right-1,left-1,-1):
                res[bottom-1][i]=c
                c+=1
            bottom-=1
            
            for i in range(bottom-1,top-1,-1):
                res[i][left]=c
                c+=1
            left+=1
        return res
