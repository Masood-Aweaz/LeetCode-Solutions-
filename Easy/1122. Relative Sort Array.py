'''********************************************************************************** 
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

 

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
**********************************************************************************'''

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        m = min(arr1)
        mx = max(arr1)
        res=[]
        c = collections.Counter(arr1)
        for i in arr2:
            for j in range(c[i]):
                res.append(i)
            del c[i]
        tmp = []
        for i in c:
            for j in range(c[i]):
                tmp.append(i)
        return res+sorted(tmp)
