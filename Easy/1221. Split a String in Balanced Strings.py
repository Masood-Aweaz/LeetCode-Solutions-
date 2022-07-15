
'''********************************************************************************** 
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
**********************************************************************************'''

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c=0
        res=0
        for i in s:
            if i == "L":
                c+=1
            else:
                c-=1
            if c==0:
                res+=1
        return res
