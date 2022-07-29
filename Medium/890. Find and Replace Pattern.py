'''********************************************************************************** 
Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

 

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.
**********************************************************************************'''

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res=[]
        flag = False
        for i in range(len(words)):
            x = zip(pattern,words[i])
            #print(x)
            d = dict()
            for j in x:
                #print(j)
                if j[0] not in d.keys():
                    if j[1] not in d.values():
                        d[j[0]]=j[1]
                        flag = True
                    elif j[1] in d.values():
                        flag = False
                        break
                elif j[0] in d.keys():
                    if d[j[0]]!=j[1]:
                        flag = False
                        break
            if flag==True:
                res.append(words[i])
        return res
