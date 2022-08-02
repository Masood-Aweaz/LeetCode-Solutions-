'''********************************************************************************** 
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
**********************************************************************************'''

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dp = dict()
        for i in range(len(nums)):
            if nums[i] not in dp:
                dp[nums[i]]=[i]
            else:
                dp[nums[i]].append(i)
        print(dp.values())
        c=0
        for i in dp.values():
            if len(i)==2:
                c+=1
            elif len(i)>2:
                for j in range(len(i)):
                    c+=len(i[j+1:])
        return c
