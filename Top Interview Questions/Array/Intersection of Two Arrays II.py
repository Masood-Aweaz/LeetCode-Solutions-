from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = Counter(nums1)&Counter(nums2)
        x = Counter(nums1)
        res=[]
        for i in counter.elements():
            res.append(i)
        return res
