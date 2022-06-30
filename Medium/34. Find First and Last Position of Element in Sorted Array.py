
'''********************************************************************************** 
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
**********************************************************************************'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        if target not in nums:
            return [-1,-1]
        res.append(nums.index(target))
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==target:
                res.append(i)
                break
        return res
