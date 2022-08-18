'''********************************************************************************** 
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
**********************************************************************************'''

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        tracked = {0:-1}        #S1
        count = 0               #S2
        max_subarray_length = 0     #S3
        
        for idx, val in enumerate(nums): #S4
            
            #a
            if val:
                count+=1 # Increment count by 1 
            else:
                count-=1 # Increment count by -1
                
            #b
            if count in tracked:
                max_subarray_length = max(max_subarray_length, idx - tracked[count])
                
            #c
            else:
                tracked[count] = idx
        
        return max_subarray_length
