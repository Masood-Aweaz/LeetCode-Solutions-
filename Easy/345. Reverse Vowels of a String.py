'''********************************************************************************** 
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

 

Example 1:

Input: s = "hello"
Output: "holle"
**********************************************************************************'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        sl=list(s)
        l = 0
        r = len(s)-1
        vow = ['a','e','i','o','u','A','E','I','O','U']
        while(l<r):
            if sl[l] not in vow:
                l+=1
            if sl[r] not in vow:
                r-=1
            elif sl[l] in vow and sl[r] in vow:
                sl[l],sl[r]=sl[r],sl[l]
                l+=1
                r-=1
        return "".join(sl)
