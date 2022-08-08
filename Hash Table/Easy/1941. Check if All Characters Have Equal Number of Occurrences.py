'''********************************************************************************** 
Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

 

Example 1:

Input: s = "abacbc"
Output: true
Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
**********************************************************************************'''

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = dict()
        for i in s:
            if i not in d:
                d[i]=s.count(i)
        return len(set(d.values()))==1
