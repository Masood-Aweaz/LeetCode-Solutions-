'''********************************************************************************** 
Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string.

An English letter b is greater than another letter a if b appears after a in the English alphabet.

 

Example 1:

Input: s = "lEeTcOdE"
Output: "E"
Explanation:
The letter 'E' is the only letter to appear in both lower and upper case.
**********************************************************************************'''

class Solution:
    def greatestLetter(self, s: str) -> str:
        res=[]
        for i in s:
            res.append(ord(i))
        #print(res)
        m=65
        char = ""
        ress=sorted(res,reverse=True)
        for i in ress:
            if i+32 in ress and i>=m :
                m = i
                char = chr(i)
        return char
                
                
        
