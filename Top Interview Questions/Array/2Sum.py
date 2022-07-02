class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        i=0
        j=0
        for i in range(l):
            j=i+1
            while(j<l):
                temp = nums[i]+nums[j]
                if temp == target:
                    return i,j
                else:
                    j=j+1
