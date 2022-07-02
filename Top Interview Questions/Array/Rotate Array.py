class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k>len(nums):
            for i in range(k):            
                nums.insert(0,nums.pop(-1))
        l = len(nums)
        index = l-k
        temp = nums
        k_i=0
        for i in range(l):
            if i >= index:
                res = temp[i]
                del nums[i]
                nums.insert(k_i,res)
                k_i+=1
                
        #print(nums)
        
