'''********************************************************************************** 
Given a sentence that consists of some words separated by a single space, and a searchWord, check if searchWord is a prefix of any word in sentence.

Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word. If searchWord is a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.

A prefix of a string s is any leading contiguous substring of s.

 

Example 1:

Input: sentence = "i love eating burger", searchWord = "burg"
Output: 4
Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.
**********************************************************************************'''

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        temp = list(sentence.split())
        print(temp)
        for i in range(len(temp)):
            if len(temp[i])==len(searchWord):
                if temp[i]==searchWord:
                    return i+1
            if len(temp[i])>len(searchWord):
                if searchWord in temp[i][:len(searchWord)]:
                    return i+1
        return -1
