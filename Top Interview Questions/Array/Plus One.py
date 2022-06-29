class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=[]
        s=""
        for i in digits:
            s=s+str(i)
        #print(s)
        temp=int(s)
        #print(temp)
        temp=temp+1
        s1=str(temp)
        #print(s1)
        for j in s1:
            res.append(j)
        return res
      
      
      
      
      
 ************************ OR ************************

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        c = 0
        if digits[l-1]!=9:
            digits[l-1]+=1
            return digits
        else:
            for i in range(l):
                if digits[l-i-1]==9:
                    digits[l-i-1]=0
                    c+=1
                else:
                    digits[l-i-1]+=1
                    return digits
        if c==l:
            digits[0]=1
            digits.append(0)
        return digits
