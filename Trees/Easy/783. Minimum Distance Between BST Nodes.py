
'''********************************************************************************** 
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
**********************************************************************************'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            nonlocal res
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        
        res = []
        inorder(root)
        print(res)
        m=10000000
        for i in range(len(res)-1):
            m = min(m,(res[i+1]-res[i]))
        print(m)
        return m
