class Solution:
    def romanToInt(self, s: str) -> int:
        count=0
        i=0
        roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        l = len(s)
        while i<l:
            if i+1<l and s[i:i+2]in roman:
                count = count+roman[s[i:i+2]]
                i=i+2
            else:
                count = count+roman[s[i]]
                i=i+1
        return count
