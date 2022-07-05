class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        snum = set(nums)
        miss = set(list(range(1,len(nums)+1)))
        res = miss - snum
        print(res)
        return list(res)
