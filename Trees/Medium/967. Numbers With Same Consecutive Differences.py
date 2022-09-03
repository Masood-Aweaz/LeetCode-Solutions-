'''********************************************************************************** 
Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.

Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.

You may return the answer in any order.

 

Example 1:

Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
**********************************************************************************'''

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        '''res = []
        
        for i in range(1,10):
            r = ""
            r+=str(i)
            for m in range(0,k+1):
                j=0
                while(len(r)<n and j<10):
                    if abs(j-int(r[-1]))==k:
                        r+=str(j)
                    else:
                        j+=1
            if len(r)==n:
                res.append(int(r))
                re = (r[::-1])
                if len(re)==n and re not in res and re[0]!='0':
                    res.append(int(re))
        print(res)
        ans = list(sorted(set(res)))
        return ans'''
        
        res = []

        def backtrack(num):
            if len(str(num)) == n:
                if num not in res:
                    res.append(num)
                return
            check = num % 10
            if (check + k) <= 9:
                num1 = (num * 10) + (check + k)
                backtrack(num1)
            if (check - k) >= 0:
                num2 = (num * 10) + (check - k)
                backtrack(num2)
        for i in range(1, 10):
            backtrack(i)
        return res
