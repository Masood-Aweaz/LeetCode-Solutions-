'''********************************************************************************** 
Given two binary strings a and b, return their sum as a binary string.
Input: a = "11", b = "1"
Output: "100"
**********************************************************************************'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=""
        if(len(a)!=len(b)):
            max_l = max(len(a),len(b))
            a = "0"*(max_l-len(a))+a
            b = "0"*(max_l-len(b))+b
        print(a)
        print(b)
        #a = a[::-1]
        #b = b[::-1]
        #print(a,b)
        carry=0
        temp=0
        
        for i in range(len(a)-1,-1,-1):
            #print(i)
            #print(a[i],b[i],carry)
            temp = int(a[i])+int(b[i])+carry
            #print(temp)
            
            if temp==2:
                res = res+'0'
                carry = 1
                temp = 0
                
            elif temp==3:
                res = res+'1'
                carry = 1
                temp = 0
            
            elif (temp==1 or temp==0):
                res = res + str(temp)
                temp=0
                carry=0
                
        if(carry==1):
            res = res + "1"
            
        return res[::-1]
                
            
