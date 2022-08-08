'''********************************************************************************** 
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
 

Example 1:

Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
**********************************************************************************'''

#from fractions import gcd
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        dp = dict()
        for i in deck:
            if i not in dp:
                dp[i]=1
            else:
                dp[i]+=1
        tmp = [i for i in dp.values() if i<2]
        if len(tmp):
            return False
        x = sorted(dp.values())
        print(x)
        c=0
        l = len(x)
        return reduce(gcd,x)>=2
        
        
