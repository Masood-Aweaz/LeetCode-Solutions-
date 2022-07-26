'''********************************************************************************** 
You are given a positive integer num consisting of exactly four digits. Split num into two new integers new1 and new2 by using the digits found in num. Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.

For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
Return the minimum possible sum of new1 and new2.

 

Example 1:

Input: num = 2932
Output: 52
Explanation: Some possible pairs [new1, new2] are [29, 23], [223, 9], etc.
The minimum sum can be obtained by the pair [29, 23]: 29 + 23 = 52.
**********************************************************************************'''

class Solution:
    def minimumSum(self, num: int) -> int:
        res=[]
        while(num):
            res.append(num%10)
            num = num//10

        res.sort()
        print(res)
        n1 = int(str(res[0])+str(res[3]))
        n2 = int(str(res[1])+str(res[2]))
        print(n1,n2)
        return n1+n2
        
