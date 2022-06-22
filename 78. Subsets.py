'''********************************************************************************** 
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
**********************************************************************************'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        #res.append([])
        for i in range(0,len(nums)+1):
            x = itertools.combinations(nums,i)
            for i in x:
                res.append(list(i))
        print(res)
        return res 
