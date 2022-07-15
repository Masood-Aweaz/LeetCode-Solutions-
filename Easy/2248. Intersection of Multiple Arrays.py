class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        temp = nums[0]
        for i in range(1,len(nums)):
            temp = list(set(temp) & set(nums[i]))
            print(temp)
        return list(temp)
            
