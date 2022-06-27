
'''********************************************************************************** 
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
**********************************************************************************'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        d_s = dict()
        d_t = dict()
        
        for i in s:
            d_s[i]=0
        for j in t:
            d_t[j]=0
            
        for k in s:
            d_s[k] = d_s[k]+1
        print(d_s)
            
        for l in t:
            d_t[l] = d_t[l]+1
            
        if d_s == d_t:
            return True
        return False
        
