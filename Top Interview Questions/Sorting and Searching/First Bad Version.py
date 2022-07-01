# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        else:
            lo = 1
            hi = n
            
            while(lo<hi):
                mid = (lo+hi)//2
                ele = lo
                x = isBadVersion(mid)
                if x == True:
                    hi = mid
                else:
                    lo = mid+1
            return lo
