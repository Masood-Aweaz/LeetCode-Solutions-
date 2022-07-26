'''********************************************************************************** 
Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.

 

Example 1:

​
Input: points = [[8,7],[9,9],[7,4],[9,7]]
Output: 1
Explanation: Both the red and the blue area are optimal.
**********************************************************************************'''

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = [i[0] for i in points]
        x = list(set(x))
        m = 0
        x.sort()
        print(x)
        for i in range(0,len(x)-1,1):
            tmp = x[i+1]-x[i]
            m = max(tmp,m)
        #print("m",m)
        return m
