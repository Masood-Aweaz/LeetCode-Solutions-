'''********************************************************************************** 
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
**********************************************************************************'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''if root:
            q = []
            count = 0
            current = root
            q.append(root)
            while len(q)>0:
                q_size = len(q)
                for i in range(q_size):
                    current = q.pop(0)
                    if current.left:
                        q.append(current.left)
                    if current.right:
                        q.append(current.right)
                count += 1
            return count
        return 0'''
        
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        if left and right:
            return 1+max(left,right)
        elif left:
            return 1+left
        return 1+right
            
        
