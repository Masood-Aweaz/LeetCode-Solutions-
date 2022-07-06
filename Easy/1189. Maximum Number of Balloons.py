'''********************************************************************************** 
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
**********************************************************************************'''


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = text.count('b')
        if b == 0 :
            return 0
        a = text.count('a')
        if a == 0 :
            return 0
        l = text.count('l')
        if l == 0 :
            return 0
        o = text.count('o')
        if o == 0 :
            return 0
        n = text.count('n')
        if n == 0 :
            return 0
        min_count = min(b,a,l//2,o//2,n)
        return min_count
