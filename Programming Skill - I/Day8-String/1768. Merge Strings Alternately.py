'''********************************************************************************** 
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.



Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
**********************************************************************************'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1=0
        w2=0
        res=""
        for i in range(len(word1)+len(word2)):
            if i%2==0 and w1<len(word1):
                res = res+word1[w1]
                w1=w1+1
            if i%2==1 and w2<len(word2):
                res = res+word2[w2]
                w2=w2+1
        if(len(word1)>len(word2)):
            res = res + word1[w1:]
        if(len(word1)<len(word2)):
            res = res + word2[w2:]
        return res
