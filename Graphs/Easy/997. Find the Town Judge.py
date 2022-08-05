'''********************************************************************************** 
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
**********************************************************************************'''

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return 1
        adj = defaultdict(list)
        for u,v in trust:
            adj[v].append(u)
            #adj[v].append(u)
        print(adj)
        res=[]
        x = [res.extend(i) for i in adj.values()]
        print(res)
        for i in adj.items() :
            if len(i[1])==n-1  and i[0] not in res:
                return i[0]
        return -1
