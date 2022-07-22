'''********************************************************************************** 
You are given a string array words and a string s, where words[i] and s comprise only of lowercase English letters.

Return the number of strings in words that are a prefix of s.

A prefix of a string is a substring that occurs at the beginning of the string. A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: words = ["a","b","c","ab","bc","abc"], s = "abc"
Output: 3
Explanation:
The strings in words which are a prefix of s = "abc" are:
"a", "ab", and "abc".
Thus the number of strings in words which are a prefix of s is 3.
**********************************************************************************'''

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        c = 0
        for i in range(len(s)+1):
            if s[:i] in words:
                c += words.count(s[:i])
        return c
