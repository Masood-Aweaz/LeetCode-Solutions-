'''********************************************************************************** 
You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

 

Example 1:

Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.
**********************************************************************************'''

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        res = n//2
        
        a = Counter(arr)
        tmp=[]
        for i in a:
            tmp.append(a[i])
        print(tmp) 
        t = sorted(tmp,reverse = True)
        total_count=0
        for index,count in enumerate(t):
            total_count+=count
            print(index,count,total_count)
            
            if total_count>=res:
                return index+1
        return 0
            
