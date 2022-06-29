class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m = len(nums)
        res = [*range(0,m+1,1)]
        print(res)
        nums.sort()
        ans = [x for x in res if x not in nums]
        return ans[0]
