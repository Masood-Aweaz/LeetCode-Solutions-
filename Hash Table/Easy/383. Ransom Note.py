'''********************************************************************************** 
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
**********************************************************************************'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = Counter(magazine)
        r = Counter(ransomNote)
        print(m,r)
        flag = False
        key=0
        for i in r.keys():
            if i in m.keys() and m[i]>=r[i] and key<len(r.keys()):
                flag = True
                key+=1
            else:
                flag = False
                break
        return flag
