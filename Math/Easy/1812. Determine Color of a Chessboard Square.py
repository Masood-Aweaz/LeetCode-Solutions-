'''********************************************************************************** 
You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.



Return true if the square is white, and false if the square is black.

The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.

 

Example 1:

Input: coordinates = "a1"
Output: false
Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.
**********************************************************************************'''

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        dp = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
        
        
        if (dp[coordinates[0]]+int(coordinates[1])-1)%2==0:
            return False
        return True
