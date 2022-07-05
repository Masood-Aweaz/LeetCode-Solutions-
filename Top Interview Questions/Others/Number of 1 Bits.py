class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0 
        while(n):
            count = count + n%2
            n>>=1
            print(n)
        return count 
       
