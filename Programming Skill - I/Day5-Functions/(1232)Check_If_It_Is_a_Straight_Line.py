
'''********************************************************************************** 
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

 


Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
**********************************************************************************'''

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        (x0, y0), (x1, y1) = coordinates[0], coordinates[1]
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (x1 - x) * (y0 - y1) != (x0 - x1) * (y1 - y):
                return False
        return True
