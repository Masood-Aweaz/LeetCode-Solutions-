'''********************************************************************************** 
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
**********************************************************************************'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        for i in s:
            if len(stack)==0 and i!="#":
                stack.append(i)
            elif i == "#":
                if len(stack)>0:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(i)
        print(stack)
        stack2 = []
        for i in t:
            if len(stack2)==0 and i!="#":
                stack2.append(i)
            elif i == "#":
                if len(stack2)>0:
                    stack2.pop()
                else:
                    continue
            else:
                stack2.append(i) 
        print(stack2)
        return stack==stack2
            
