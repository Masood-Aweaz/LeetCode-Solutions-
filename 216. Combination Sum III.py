'''********************************************************************************** 
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.


Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
**********************************************************************************'''

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1,10))
        res=[]
        #print(nums)
        x = itertools.combinations(nums,k)
        for i in x:
            if sum(i)==n:
                res.append(i)
        return res
