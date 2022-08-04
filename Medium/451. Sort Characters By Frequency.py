'''********************************************************************************** 
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
**********************************************************************************'''

class Solution:
    def frequencySort(self, s: str) -> str:
        d = dict()
        for i in s:
            ind = s.index(i)
            if ind not in d:
                d[ind]=1
            else:
                d[ind]+=1
        #print(d)
        tmp = dict(sorted(d.items(),key=lambda i:(i[1],-i[0])))
        #print(tmp)
        res = ""
        for i in tmp.keys():
            #print(type(i))
            res += s[i]*tmp[i]
        #print(res)
        return res[::-1]
