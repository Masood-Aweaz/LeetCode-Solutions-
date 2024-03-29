'''********************************************************************************** 
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.

 

Example 1:

Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.
**********************************************************************************'''

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dp = {}
        for i in nums:
            if i not in dp:
                dp[i]=1
            else:
                dp[i]+=1
        x = [i for i in dp if dp[i]==1]
        return sum(x)
