'''********************************************************************************** 
You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.

 

Example 1:

Input: nums = [3,2,3,2,2,2]
Output: true
Explanation: 
There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.
**********************************************************************************'''

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        p = len(nums)/2
        d = dict()
        for i in nums:
            if i not in d:
                d[i]=nums.count(i)%2
        print(d)
        if sum(list(d.values()))==0:
            return True
        else:
            return False
                
