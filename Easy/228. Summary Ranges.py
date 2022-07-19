'''********************************************************************************** 
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
**********************************************************************************'''

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        arr=[]
        if len(nums)==0:
            return []
        if len(nums)==1:
            arr.append(str(nums[0]))
            return arr
        start = nums[0]
     
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]!=1:
                print(nums[i],nums[i-1])
                if start != nums[i-1]:
                    res = str(start)+"->"+str(nums[i-1])
                else:
                    res = str(start)
                arr.append(res)
                res=""
                start = nums[i]
            if nums[i]-nums[i-1]==1 and i==len(nums)-1:
                if start != nums[i]:
                    res = str(start)+"->"+str(nums[i])
                else:
                    res = str(start)
                arr.append(res)
            if nums[i]-nums[i-1]!=1 and i == len(nums)-1:
                if start != nums[i]:
                    res = str(start)+"->"+str(nums[i])
                else:
                    res = str(start)
                arr.append(res)
        print(arr)
        return arr
