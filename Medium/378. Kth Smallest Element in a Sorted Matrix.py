'''********************************************************************************** 
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

 

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
**********************************************************************************'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l, r, N = matrix[0][0], matrix[-1][-1], len(matrix)
        
        def less_k(m):
            cnt = 0 # count
            for r in range(N):
                # binary search 
                x = bisect_right(matrix[r], m)
                cnt += x
            return cnt
        
        while l<r:
            mid = (l+r) // 2
            
            if less_k(mid) < k:
                l = mid + 1
            else:
                r = mid
        return l
                
            
        
