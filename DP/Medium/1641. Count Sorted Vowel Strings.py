'''********************************************************************************** 
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

 

Example 1:

Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
**********************************************************************************'''


class Solution:
    def countVowelStrings(self, n: int) -> int:
        aCount = [1]*n
        eCount = [1]*n
        iCount = [1]*n
        oCount = [1]*n
        uCount = [1]*n
        
        for i in range(1,n):
            aCount[i] = aCount[i-1]+eCount[i-1]+iCount[i-1]+oCount[i-1]+uCount[i-1]
            eCount[i] = eCount[i-1]+iCount[i-1]+oCount[i-1]+uCount[i-1]
            iCount[i] = iCount[i-1]+oCount[i-1]+uCount[i-1]
            oCount[i] = oCount[i-1]+uCount[i-1]
            uCount[i] = uCount[i-1]
        result = aCount[-1]+eCount[-1]+iCount[-1]+oCount[-1]+uCount[-1]
        
        return result
            
