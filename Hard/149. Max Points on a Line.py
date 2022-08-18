'''********************************************************************************** 
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 

Example 1:


Input: points = [[1,1],[2,2],[3,3]]
Output: 3
**********************************************************************************'''

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        d = {}
        m = 0
        for i in range(len(points)-m-1):
            i_max=0
            for j in range(i+1,len(points)):
                if points[j][0]-points[i][0]==0:
                    slope = 10000000001
                else:
                    slope = (float)(points[j][1]-points[i][1])/(float)(points[j][0]-points[i][0])
                    
                if slope in d.keys():
                    d[slope]+=1
                else:
                    d[slope]=1
                i_max = i_max if i_max>d[slope] else d[slope]
            d.clear()
            m = m if i_max<m else i_max
        return m+1
                    
                    
