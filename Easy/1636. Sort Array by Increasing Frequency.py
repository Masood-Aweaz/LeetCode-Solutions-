'''********************************************************************************** 
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

 

Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
**********************************************************************************'''

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort()
        x = dict()
        res=[]
        for i in range(len(nums)):
            ind=nums.index(nums[i])
            if ind not in x:
                x[ind]=1
            else:
                x[ind]+=1
        print(x)
        
        tmp = dict(sorted(x.items(),key=lambda i:(i[1],-i[0])))
        print(tmp)
        for i in tmp.keys():
            res.extend([nums[i]]*tmp[i])
        print(res)
        return res
