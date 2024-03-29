'''********************************************************************************** 
A string is good if there are no repeated characters.

Given a string s, return the number of good substrings of length three in s.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".
**********************************************************************************'''

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(0,len(s)-2):
            #print(s[i:i+3])
            tmp = sorted(list(s[i:i+3]))
            stmp = sorted(list(set(tmp)))
            print(tmp,stmp)
            if len(tmp)==len(stmp):
                count+=1
        return count
