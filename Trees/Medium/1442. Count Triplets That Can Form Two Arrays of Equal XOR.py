
'''********************************************************************************** 
Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.

 

Example 1:

Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
**********************************************************************************'''

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        for i in range(len(arr)):
            curr = arr[i]
            for j in range(i+1,len(arr)):
                curr^=arr[j]
                if curr == 0:
                    ans+=j-i
        return ans
