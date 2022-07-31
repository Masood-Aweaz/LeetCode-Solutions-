'''********************************************************************************** 
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

 

Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]
**********************************************************************************'''

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        d = dict()
        ans = set(words1)
        for i in words2:
            for j in i:
                count = i.count(j)
                if j not in d or count>d[j]:
                    d[j]=count
        print(d)
        for i in words1:
            for j in d:
                if i.count(j)<d[j]:
                    ans.remove(i)
                    break
        return list(ans)
