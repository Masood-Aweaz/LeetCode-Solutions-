'''********************************************************************************** 
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
**********************************************************************************'''

class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        n = len(height)
       
        maxHeight_left = [0]*n
        m = height[0]
        for i in range(n):
            if height[i]>m:
                m = height[i]
            maxHeight_left[i]=m
            
        maxHeight_right = [0]*n
        m = height[-1]
        for i in reversed(range(n)):
            if height[i]>m:
                m = height[i]
            maxHeight_right[i]=m
            
        for i in range(n):
            water = water + min(maxHeight_left[i],maxHeight_right[i]) - height[i]
        return water
