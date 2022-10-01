'''********************************************************************************** 
You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.

 

Example 1:

Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.
**********************************************************************************'''

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        x = zip(names,heights)
        print(x)
        s = sorted(x,key=lambda i:i[1],reverse=True)
        res=[]
        for z in s:
            res.append(z[0])
        return res
