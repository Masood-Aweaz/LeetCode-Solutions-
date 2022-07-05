'''********************************************************************************** 
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
**********************************************************************************'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        longest = 1
        streak = 1
        
        nums.sort()
        
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                if nums[i]==nums[i-1]+1:
                    streak += 1
                else:
                    longest = max(longest,streak)
                    streak = 1
        return max(longest,streak)
                
            
