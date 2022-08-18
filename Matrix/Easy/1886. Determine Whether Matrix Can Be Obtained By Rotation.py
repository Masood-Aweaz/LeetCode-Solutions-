'''********************************************************************************** 
Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

 

Example 1:


Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
**********************************************************************************'''

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
                
        if mat==target:
            return True
        
        for i in range(3):
            self.transpose(mat)
            self.reflect(mat)
            if mat==target:
                return True
        return False
    
    
    def transpose(self,mat):
        for i in range(len(mat)):
            for j in range(i+1,len(mat)):
                mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
                
                
    def reflect(self,mat):
        for i in range(len(mat)):
            mat[i].reverse()
    
    
            
            
    
