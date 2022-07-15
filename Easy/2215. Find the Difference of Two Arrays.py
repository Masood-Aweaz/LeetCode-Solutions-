class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans=[]
        temp=[]
        ans.append(list(set(nums1)-set(nums2)))
        ans.append(list(set(nums2)-set(nums1)))
        print(ans)
        return ans 
