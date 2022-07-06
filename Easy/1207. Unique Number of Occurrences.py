'''********************************************************************************** 
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
**********************************************************************************'''

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
        x = list(d.values())
        n = len(x)
        setx = set(x)
        m = len(list(setx))
        if n==m:
            return True
        else:
            return False
        
