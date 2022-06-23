'''********************************************************************************** 
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).


Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
**********************************************************************************'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        print(nums1)
        l = len(nums1)
        print(l)
        if(l==1):
            return nums1[0]
        elif(l%2!=0):
            return nums1[l/2]
        elif(l%2==0):
            return float((nums1[l/2]+nums1[(l/2)-1])/2.0)
