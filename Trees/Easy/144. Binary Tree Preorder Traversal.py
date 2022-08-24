'''********************************************************************************** 
Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
**********************************************************************************'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = [root]
        res=[]
        while q:
            l = len(q)
            #for i in range(l):
            tmp = q.pop()
            if tmp:
                res.append(tmp.val)
                #if tmp.left:
                q.append(tmp.right)
                #if tmp.right:
                q.append(tmp.left)
        return res
                    
