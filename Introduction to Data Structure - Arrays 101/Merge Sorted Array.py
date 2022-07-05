class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        '''temp = nums1[:m]
        #print(temp)
        for i in nums2:
            temp.append(i)
        #print(temp)
        temp.sort()
        #print(temp)
        for i in range(len(temp)):
            nums1[i]=temp[i]'''
        
        for i in range(n):
            nums1[m+i]=nums2[i]
        nums1.sort()
    
            
                

