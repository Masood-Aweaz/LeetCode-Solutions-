'''********************************************************************************** 
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.



Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".
**********************************************************************************'''

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        mis_ind = []
        if(s1==s2):
            return True
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                mis_ind.append(i)
        if(len(mis_ind)>2):
            return False
        elif(len(mis_ind)==1):
            return False
        elif(len(mis_ind)==2):
            if ((s1[mis_ind[0]]==s2[mis_ind[1]]) and (s1[mis_ind[1]]==s2[mis_ind[0]])):
                return True
            else:
                return False 
            
