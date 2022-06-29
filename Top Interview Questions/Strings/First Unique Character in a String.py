class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = dict()
        for i in (s):
            if i not in d.keys():
                d[i]=1
            else:
                d[i]+=1
        print(d)
        for k in d.keys():
            if d[k]==1:
                ele = k
                return s.index(ele)
        return -1
        
