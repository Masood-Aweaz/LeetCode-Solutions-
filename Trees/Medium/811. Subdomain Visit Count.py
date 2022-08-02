
'''********************************************************************************** 
A website domain "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com" and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3" or "rep d1.d2" where rep is the number of visits to the domain and d1.d2.d3 is the domain itself.

For example, "9001 discuss.leetcode.com" is a count-paired domain that indicates that discuss.leetcode.com was visited 9001 times.
Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each subdomain in the input. You may return the answer in any order.

 

Example 1:

Input: cpdomains = ["9001 discuss.leetcode.com"]
Output: ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
Explanation: We only have one website domain: "discuss.leetcode.com".
As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.
**********************************************************************************'''

class Solution:
    def subdomainVisits(self, cpd: List[str]) -> List[str]:
        res=[]
        d=dict()
        for i in cpd:
            x = i.split(" ")
            #print(x)
            x1  = x[0]
            x2 = x[1].split(".")
            #print(x2)
            l = len(x2)
            for j in range(l):
                tmp = x[1].split(".",j)
                #print(tmp[j])
                if tmp[j] not in d:
                    d[tmp[j]]=int(x1)
                else:
                    d[tmp[j]]+=int(x1)
                
        print(d)
        for k in d.items():
            res.append((str(k[1])+" "+k[0]))
        print(res)
        return res
