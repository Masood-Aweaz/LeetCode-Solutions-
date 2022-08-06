'''********************************************************************************** 
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
**********************************************************************************'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        m = 111111111111
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue 
                
            l = i+1
            r = len(nums)-1
            while(l<r):
                s = nums[i]+nums[l]+nums[r]
                if abs(target-s)<m:
                    m=abs(target-s)
                    ans = s
                if s<target:
                    l+=1
                elif s>target:
                    r-=1
                else:
                    return target
        return ans
                    
        
        
