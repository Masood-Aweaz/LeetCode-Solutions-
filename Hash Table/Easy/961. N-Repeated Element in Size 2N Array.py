'''********************************************************************************** 
You are given an integer array nums with the following properties:

nums.length == 2 * n.
nums contains n + 1 unique elements.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times.

 

Example 1:

Input: nums = [1,2,3,3]
Output: 3
**********************************************************************************'''

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        dp = {}
        for i in nums:
            if i not in dp:
                dp[i]=1
            else:
                return i
