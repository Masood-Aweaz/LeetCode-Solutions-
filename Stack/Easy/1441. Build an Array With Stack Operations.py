
'''********************************************************************************** 
You are given an array target and an integer n.

In each iteration, you will read a number from list = [1, 2, 3, ..., n].

Build the target array using the following operations:

"Push": Reads a new element from the beginning list, and pushes it in the array.
"Pop": Deletes the last element of the array.
If the target array is already built, stop reading more elements.
Return a list of the operations needed to build target. If there are multiple valid answers, return any of them.

 

Example 1:

Input: target = [1,3], n = 3
Output: ["Push","Push","Pop","Push"]
Explanation: 
Read number 1 and automatically push in the array -> [1]
Read number 2 and automatically push in the array then Pop it -> [1]
Read number 3 and automatically push in the array -> [1,3]
**********************************************************************************'''

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        num = list(range(1,n+1))
        res=[]
        ans=[]
        for i in num:
            res.append(i)
            ans.append("Push")
            if i not in target:
                res.pop()
                ans.append("Pop")
            if res==target:
                break
            print(res,ans)
        return ans
