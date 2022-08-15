
'''********************************************************************************** 
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

 

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
**********************************************************************************'''

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        res=""
        for i in range(len(s)):
            if len(stack)==0:
                stack.append([s[i],1])
            elif stack[-1][0]==s[i]:
                stack[-1][1]=stack[-1][1]+1
            else:
                stack.append([s[i],1])
            if stack[-1][1]==k:
                stack.pop()
        for i in stack:
            res+=i[0]*i[1]
        return res
            
                
                
