#https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1


#User function Template for python3


class Solution:
    def __init__(self):
        self.res = []
  
    def isSafe(self,matrix,i,j,visited,n):
        if i<0 or i>=n or j < 0 or j>=n or matrix[i][j] == 0 or visited[i][j] == 1:
            return False 
        return True 
  
    def pop(self,path):
        path = path[:len(path)-1]
        
    def solve(self,matrix,i,j,path,visited,n):
        
        if i== n-1 and j==n-1:
          self.res.append(path)
          return 
        
        visited[i][j] = 1 
        
        leftSafe = self.isSafe(matrix,i,j-1,visited,n)
        rightSafe = self.isSafe(matrix,i,j+1,visited,n)
        downSafe = self.isSafe(matrix,i+1,j,visited,n)
        upSafe = self.isSafe(matrix,i-1,j,visited,n)
        
        if downSafe:
          self.solve(matrix,i+1,j,path+"D",visited,n) 
          self.pop(path)
        
        if leftSafe: 
          self.solve(matrix,i,j-1,path+"L",visited,n)
          self.pop(path)
        
        if rightSafe:
          self.solve(matrix,i,j+1,path+"R",visited,n)
          self.pop(path)
        
        if upSafe:
          self.solve(matrix,i-1,j,path+"U",visited,n) 
          self.pop(path)
       
        visited[i][j] = 0
        
        
    def findPath(self,matrix,n):
        visited = [[0 for j in range(n)] for i in range(n)]
        if matrix[0][0] == 0 or matrix[n-1] [n-1] == 0:
          return []
        i=j=0 
        self.solve(matrix,i,j,'',visited,n)
        return sorted(self.res)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends
