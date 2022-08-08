'''********************************************************************************** 
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

 

Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
**********************************************************************************'''

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dp = dict()
        res = []
        for i in paths:
            res.extend(i)
        print(res)
        for i in set(res):
            if i not in dp:
                dp[i]=[]
        for i in paths:
            dp[i[0]].append(i[1])
        x = [i[0] for i in dp.items() if i[1]==[]]
        print(x)
        return "".join(x)
