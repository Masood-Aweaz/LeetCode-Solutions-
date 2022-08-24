'''********************************************************************************** 
A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

 

Example 1:


Input: root = [1,1,1,1,1,null,1]
Output: true
**********************************************************************************'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.s = set()
        def dfs(node):
            if not node:
                return 
            self.s.add(node.val)
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        print(self.s)
        return len(self.s)==1
