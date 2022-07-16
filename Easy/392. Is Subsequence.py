'''********************************************************************************** 
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
**********************************************************************************'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        
        if len(s)>len(t):
            return False
        if len(s)==0:
            return True
        sub = 0
        for i in range(0,len(t)):
            if sub <= len(s)-1:
                if s[sub]==t[i]:
                    sub+=1
        return sub == len(s)
