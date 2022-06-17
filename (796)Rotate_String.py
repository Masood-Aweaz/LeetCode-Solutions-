'''********************************************************************************** 
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.

Input: s = "abcde", goal = "cdeab"
Output: true
**********************************************************************************'''

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        l = len(s)
        count=0
        while(count<l):
            if s==goal:
                return True
            else:
                print(s)
                s = s + s[0]
                s=s[1:]
                print(s)
                count=count+1
        return False
