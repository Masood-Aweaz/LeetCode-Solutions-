'''********************************************************************************** 
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
**********************************************************************************'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        digit = []
        i = len(num1)-1
        j = len(num2)-1
        while i>=0 and j>=0:
            num = int(num1[i])+int(num2[j])+carry
            digit.append(str(num%10))
            carry = num//10
            i-=1
            j-=1
        while i>=0:
            num = carry+int(num1[i])
            digit.append(str(num%10))
            carry = num//10
            i-=1
        while j>=0:
            num = carry+int(num2[j])
            digit.append(str(num%10))
            carry = num//10
            j-=1
        if carry:
            digit.append(str(carry))
        return "".join(digit[::-1])
         
                
