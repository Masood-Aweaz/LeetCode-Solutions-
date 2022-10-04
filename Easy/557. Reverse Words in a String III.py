
'''********************************************************************************** 
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
**********************************************************************************'''

class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split(" ")
        print(x)
        res=""
        for i in x:
            res+=i[::-1]
            res+=" "
        print(res)
        return res[:len(s)]
