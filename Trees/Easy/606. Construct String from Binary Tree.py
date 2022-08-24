'''********************************************************************************** 
Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

 

Example 1:


Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"
**********************************************************************************'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        s = ""
        if root==None:
            return ""
        if root.left==None and root.right==None:
            return str(root.val)+""
        if root.right==None:
            return str(root.val)+"("+self.tree2str(root.left)+")"
        return str(root.val)+"("+self.tree2str(root.left)+")("+self.tree2str(root.right)+")"
