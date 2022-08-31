
'''********************************************************************************** 
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
**********************************************************************************'''

class Solution:
    def pacificAtlantic(self, ht: List[List[int]]) -> List[List[int]]:
        
        def pac(i,j):
            if rp[i][j]:
                return True
            k=False
            h=ht[i][j]
            ht[i][j]=100001
            if ht[i-1][j]<=h:
                k=k or pac(i-1,j)
                
            if ht[i][j-1]<=h:
                k=k or pac(i,j-1)
                
            if i<m-1 and ht[i+1][j]<=h:
                k=k or pac(i+1,j)
                
            if j<n-1 and ht[i][j+1]<=h:
                k=k or pac(i,j+1)
                
            ht[i][j]=h
            rp[i][j]=k
            return k
        
        def ant(i,j):
            if ra[i][j]:
                return True
            k=False
            h=ht[i][j]
            ht[i][j]=100001
            if i>0 and ht[i-1][j]<=h:
                k=k or ant(i-1,j)
                
            if j>0 and ht[i][j-1]<=h:
                k=k or ant(i,j-1)
                
            if ht[i+1][j]<=h:
                k=k or ant(i+1,j)
                
            if ht[i][j+1]<=h:
                k=k or ant(i,j+1)
                
            ht[i][j]=h
            ra[i][j]=k
            return k
        
        m=len(ht)
        n=len(ht[0])
        rp=[[False for i in range(n)] for j in range(m)]
        ra=[[False for i in range(n)] for j in range(m)]
        
        for i in range(m):
            rp[i][0]=True
            ra[i][-1]=True
        for i in range(n):
            rp[0][i]=True
            ra[-1][i]=True
        
        for i in range(m):
            for j in range(n):
                pac(i,j)
                ant(i,j)
        res=[]
        for i in range(m):
            for j in range(n):
                if rp[i][j] and ra[i][j]:
                    res.append([i,j])
        return res
