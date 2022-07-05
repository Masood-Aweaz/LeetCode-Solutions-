class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [x*x for x in nums]
        #print(res)
        res.sort()
        return res
