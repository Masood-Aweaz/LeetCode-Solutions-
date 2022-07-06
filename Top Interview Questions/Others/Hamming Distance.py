class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bin = bin(x)[2:]
        y_bin = bin(y)[2:]
        #print(x_bin.zfill(4))
        #print(y_bin.zfill(4))
        xl = len(x_bin)
        yl = len(y_bin)
        m = max(xl,yl)
        x = x_bin.zfill(m)
        y = y_bin.zfill(m)
        print(x,y)
        count=0
        for i in range(m):
            if x[i]!=y[i]:
                count+=1
        return count
