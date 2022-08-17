# https://practice.geeksforgeeks.org/problems/thief-try-to-excape0710/1#


#User function Template for python3

class Solution:
    def totalJumps(self, X, Y, N, arr):
        # code here
        jump = X-Y
        c=0
        for i in arr:
            while(i>X):
                i = i-(X-Y)
                c+=1
            if i <= X and i!=0:
                c+=1
        #print(c)
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        X, Y, N = [int(x) for x in input().split()]
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.totalJumps(X, Y, N, arr))
# } Driver Code Ends
