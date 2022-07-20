'''********************************************************************************** 
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
**********************************************************************************'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        d = dict()
        res=[]
        for i in nums:
            if i not in d:
                d[i] = nums.count(i)
        print(d)
        dv = d.values()
        l = sorted(dv,reverse=True)
        print(l)
        j=0
        for i in range(k):
            x = (list(d.keys())[list(d.values()).index(l[i])])
            del d[x]
            res.append(x)
        print(res)
        return res
