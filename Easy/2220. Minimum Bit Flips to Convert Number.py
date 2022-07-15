class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        sb = bin(start)[2:]
        gb = bin(goal)[2:]
        l = max(len(sb),len(gb))
        s = sb.zfill(l)
        g = gb.zfill(l)
        print(s,g)
        c = 0
        for i in range(len(s)):
            if s[i]!=g[i]:
                c+=1
        return c
