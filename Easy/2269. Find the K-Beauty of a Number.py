'''********************************************************************************** 
The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that meet the following conditions:

It has a length of k.
It is a divisor of num.
Given integers num and k, return the k-beauty of num.

Note:

Leading zeros are allowed.
0 is not a divisor of any value.
A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: num = 240, k = 2
Output: 2
Explanation: The following are the substrings of num of length k:
- "24" from "240": 24 is a divisor of 240.
- "40" from "240": 40 is a divisor of 240.
Therefore, the k-beauty is 2.
**********************************************************************************'''

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        snum = str(num)
        count = 0 
        for i in range(0,len(snum)):
            #print(i)
            temp = int(snum[i:k+i])
            print(temp)
            
            if temp!=0 and num%temp==0:
                count+=1
            if k+i == len(snum):
                break
        return count
