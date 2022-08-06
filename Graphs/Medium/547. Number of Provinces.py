'''********************************************************************************** 
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
**********************************************************************************'''

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj = collections.defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i!=j and isConnected[i][j]==1:
                    adj[i].append(j)
        print(adj)
        
        
        def bfs(node):
            queue = collections.deque()
            queue.append(node)
            visited.add(node)
            
            while queue:
                curr = queue.popleft()
                for neigh in adj[curr]:
                    if neigh not in visited:
                        queue.append(neigh)
                        visited.add(neigh)
        
        visited = set()
        prov =0
        for ind in range(n):
            if ind not in visited:
                bfs(ind)
                prov+=1
        return prov
                
                    
