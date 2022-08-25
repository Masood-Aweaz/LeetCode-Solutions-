'''********************************************************************************** 
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
 

Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
**********************************************************************************'''

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        
        if s==goal:
            seen=set()
            for a in s:
                if a in seen:
                    return True
                seen.add(a)
            print(seen)
            return False
        
        
        pairs = []
        for a, b in zip(s, goal):
            if a != b:
                pairs.append((a, b))
            if len(pairs) >= 3: 
                return False
        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]
             
