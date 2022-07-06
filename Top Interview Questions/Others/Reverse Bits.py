class Solution:
    def reverseBits(self, n: int) -> int:
        bin_n = bin(n)[2:]
        str_n = f'{bin_n}'
        #print((str_n))
        x = str_n.zfill(32)
        #print(x)
        #print(x[::-1])
        rx = x[::-1]
        return int(rx,2)
        
        
