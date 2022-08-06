'''********************************************************************************** 
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
**********************************************************************************'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            for j in range(len(nums)-1,-1,-1):
                l = i+1
                r = j-1
                while(l<r):
                    if nums[i]+nums[j]+nums[l]+nums[r]==target:
                        if [nums[i],nums[j],nums[l],nums[r]] not in res:
                            res.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                    if nums[i]+nums[j]+nums[l]+nums[r]<target:
                        l+=1
                    if nums[i]+nums[j]+nums[l]+nums[r]>target:
                        r-=1
        print(res)
        return res
