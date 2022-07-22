'''********************************************************************************** 
You are given a string number representing a positive integer and a character digit.

Return the resulting string after removing exactly one occurrence of digit from number such that the value of the resulting string in decimal form is maximized. The test cases are generated such that digit occurs at least once in number.

 

Example 1:

Input: number = "123", digit = "3"
Output: "12"
Explanation: There is only one '3' in "123". After removing '3', the result is "12".
**********************************************************************************'''

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        maxnum = 0
        for i in range(len(number)):
            if number[i]==digit:
                maxnum = max(maxnum,int(("".join(number[:i])+("".join(number[i+1:])))))
        return str(maxnum)
