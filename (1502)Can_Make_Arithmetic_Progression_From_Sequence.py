'''********************************************************************************** 
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.


Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
**********************************************************************************'''

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1]-arr[0]
        #print(diff)
        for i in range(1,len(arr)-1,2):
            #print((arr[i+1]-arr[i]))
            if ((arr[i+1]-arr[i])!=diff):
                return False
        return True
            
