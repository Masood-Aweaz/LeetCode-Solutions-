
'''********************************************************************************** 
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
**********************************************************************************'''

import numpy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''ans = []
        for i in range(len(nums)):
            #ans.append(int(numpy.prod(nums[:i])*numpy.prod(nums[i+1:])))
            temp = nums[i]
            #print(nums)
            nums.remove(nums[i])
            #print(nums)
            ans.append(int(numpy.prod(nums)))
            #print(ans)
            nums.insert(i,temp)
            #print(nums)
        print(ans)
        return ans'''
        n = len(nums)
        left = [1]*n
        right = [1]*n
        
        for i in range(1,n):
            left[i] = left[i-1]*nums[i-1]
            right[n-1-i] = right[n-i]*nums[n-i]
        
        print(left,right)
        
        ans=[1]*n
        for j in range(n):
            ans[j] = left[j]*right[j]
        
        return ans
