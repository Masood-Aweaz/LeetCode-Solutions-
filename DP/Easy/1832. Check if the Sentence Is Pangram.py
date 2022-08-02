
'''********************************************************************************** 
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
**********************************************************************************'''

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        l = len(sentence)
        if l<26:
            return False
        d=dict()
        for i in range(97,97+26):
            d[chr(i)]=0
        print(d)
        for i in sentence:
            d[i]+=1
        print(d.values())
        return 0 not in d.values()
