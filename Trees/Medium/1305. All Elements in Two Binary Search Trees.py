'''********************************************************************************** 
Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

 

Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
**********************************************************************************'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.res = []
        
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            self.res.append(node.val)
            inorder(node.right)
            
        inorder(root1)
        inorder(root2)
        self.res.sort()
        return self.res
