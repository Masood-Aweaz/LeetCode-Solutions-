class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0,nums[0]]
        for i in range(1,len(nums)):
            dp.append(max(dp[i],nums[i]+dp[i-1]))
            print(dp)
        return dp[len(nums)]
