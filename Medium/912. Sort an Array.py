'''********************************************************************************** 
Given an array of integers nums, sort the array in ascending order.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
**********************************************************************************'''

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        dp = collections.Counter(nums)
        m = min(nums)
        mx = max(nums)
        res=[]
        for i in range(m,mx+1):
            if i in dp:
                for j in range(dp[i]):
                    res.append(i)
        return res
