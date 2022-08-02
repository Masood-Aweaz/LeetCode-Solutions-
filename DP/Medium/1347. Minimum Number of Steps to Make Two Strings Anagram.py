
'''********************************************************************************** 
You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

 

Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
**********************************************************************************'''

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ds = dict()
        for i in s:
            if i not in ds:
                ds[i]=1
            else:
                ds[i]+=1
        print(ds)
        dt=dict()
        for i in t:
            if i in ds:
                if ds[i]>0:
                    ds[i]-=1
                else:
                    if i not in dt:
                        dt[i]=1
                    else:
                        dt[i]+=1
            else:
                if i not in dt:
                    dt[i]=1
                else:
                    dt[i]+=1
                    
        print(ds,dt)
        return sum(dt.values())
