
'''********************************************************************************** 
Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

A subarray is a contiguous subsequence of the array.



Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
**********************************************************************************'''


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        tsum = 0 
        for i in range(len(arr)):
            for j in range(i+1,len(arr)+1):
                if(len(arr[i:j]))%2==1:
                    tsum = tsum+sum(arr[i:j])
        return tsum
