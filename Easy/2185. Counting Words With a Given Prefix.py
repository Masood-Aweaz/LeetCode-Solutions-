'''********************************************************************************** 
You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.

 

Example 1:

Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
**********************************************************************************'''

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        c=0
        for i in range(len(words)):
            x = words[i].startswith(pref)
            if x == True:
                c+=1
        return c
