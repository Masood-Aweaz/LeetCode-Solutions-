'''********************************************************************************** 
Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.
 

Example 1:

Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
Output: [3,2]
Explanation: The values that are present in at least two arrays are:
- 3, in all three arrays.
- 2, in nums1 and nums2.
**********************************************************************************'''

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        dp = dict()
        for i in set(nums1):
            if i not in dp:
                dp[i]=1
                
        for i in set(nums2):
            if i in dp:
                dp[i]+=1
            else:
                dp[i]=1
        
        for i in set(nums3):
            if i in dp:
                dp[i]+=1
            else:
                dp[i]=1
        
        print(dp)
        res=[]
        for i in dp:
            if dp[i]>=2:
                res.append(i)
        return res
