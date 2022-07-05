class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        count1=0
        for i in range  (0,len(nums)):
            if nums[i]==1:
                count1+=1
                count=max(count,count1)
            else : count1=0
        return count
                
            
