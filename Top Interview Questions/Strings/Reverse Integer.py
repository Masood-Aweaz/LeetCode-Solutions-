class Solution:
    def reverse(self, x: int) -> int:
        s = ""
        res=[]
        sign=0
        if x < 1: 
            sign = -1
            x = abs(x)
        if x<=9:
            return x
        while(x):
            temp = x%10
            x = x//10
            s = s + str(temp)
        print(s)
        s = int(s)
        if(-2**31<=s<=(2**31)-1):
            if sign==-1:
                return -s
            else:
                return s
        else:
            return 0
