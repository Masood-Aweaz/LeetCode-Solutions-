'''********************************************************************************** 
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

 

Example 1:


Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
**********************************************************************************'''

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        def build(arr):
            graph = {}
            for edge in arr:
                a, b = edge[0], edge[1]
                if a not in graph:
                    graph[a] = []
                if b not in graph:
                    graph[b] = []
                graph[a].append(b)
                graph[b].append(a)
            return graph
    
        x = build(edges)
        print(x)
        n = len(edges)
        for i in x.items():
            if len(i[1]) == n:
                return i[0]
