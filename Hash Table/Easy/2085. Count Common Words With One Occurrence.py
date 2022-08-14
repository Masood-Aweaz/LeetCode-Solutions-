'''********************************************************************************** 
Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.

 

Example 1:

Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
Output: 2
Explanation:
- "leetcode" appears exactly once in each of the two arrays. We count this string.
- "amazing" appears exactly once in each of the two arrays. We count this string.
- "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
- "as" appears once in words1, but does not appear in words2. We do not count this string.
Thus, there are 2 strings that appear exactly once in each of the two arrays.
**********************************************************************************'''
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dp = dict()
        '''words1.extend(words2)
        x = Counter(words1)
        print(x)
        c=0
        for i in x:
            if x[i]==2:
                c+=1
        return c'''
        
        for i in words1:
            if i not in dp:
                dp[i]=1
            else:
                dp[i]+=1
        print(dp)
        x = set([i for i in dp.keys() if dp[i]==1])
        
        dp2 = dict()
        for i in words2:
            if i not in dp2:
                dp2[i]=1
            else:
                dp2[i]+=1
        y = set([i for i in dp2.keys() if dp2[i]==1])
        
        tmp = x.intersection(y)
        print(tmp)
        return len(tmp)
            
