'''********************************************************************************** 
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
**********************************************************************************'''

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l_s1 = s1.split(" ")
        l_s2 = s2.split(" ")
        l_s1.sort()
        l_s2.sort()
        count = {}
        for i in l_s1:
            count[i] = count.get(i,0)+1
        for j in l_s2:
            count[j] = count.get(j,0)+1
        
        return [word for word in count if count[word]==1]
                
            
