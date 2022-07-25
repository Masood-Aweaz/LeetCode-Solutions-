'''********************************************************************************** 
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
**********************************************************************************'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        res = []
        def check(root1,root2):
            if root1==None and root2==None:
                return 
            if root1==None or root2==None:
                res.append(1)
                return 
            if root1.val!=root2.val:
                res.append(1)
                return
            check(root1.left,root2.right)
            check(root1.right,root2.left)
        
        check(root.left,root.right)
        if 1 in res:
            return False
        else:
            return True
         
