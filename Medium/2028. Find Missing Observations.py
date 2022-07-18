'''********************************************************************************** 
You have observations of n + m 6-sided dice rolls with each face numbered from 1 to 6. n of the observations went missing, and you only have the observations of m rolls. Fortunately, you have also calculated the average value of the n + m rolls.

You are given an integer array rolls of length m where rolls[i] is the value of the ith observation. You are also given the two integers mean and n.

Return an array of length n containing the missing observations such that the average value of the n + m rolls is exactly mean. If there are multiple valid answers, return any of them. If no such array exists, return an empty array.

The average value of a set of k numbers is the sum of the numbers divided by k.

Note that mean is an integer, so the sum of the n + m rolls should be divisible by n + m.

 

Example 1:

Input: rolls = [3,2,4,3], mean = 4, n = 2
Output: [6,6]
Explanation: The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.
**********************************************************************************'''

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        res = []
        total = len(rolls)+n
        miss = (mean*total)-sum(rolls)
        if miss<n or miss>n*6:
            return res
        #print(miss)
        while(miss):
            dice = min(miss-n+1,6)
            res.append(dice)
            miss -= dice
            n -= 1
        return res
