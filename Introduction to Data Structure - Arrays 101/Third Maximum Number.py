class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        snum = set(nums)
        lnum = list(snum)
        n = len(lnum)
        lnum.sort()
        print(lnum)
        if n==3:
            return lnum[0]
        elif n>3:
            return lnum[-3]
        else:
            return max(lnum)
