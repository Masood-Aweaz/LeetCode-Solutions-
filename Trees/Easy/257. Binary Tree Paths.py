'''********************************************************************************** 
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

 

Example 1:


Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
**********************************************************************************'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        temp = [(root,str(root.val))]
        res = []
        
        while temp:
            node,path = temp.pop()
            
            if node.left==None and node.right==None:
                res.append(path)
                continue
            if node.left:
                temp.append((node.left,path+"->"+str(node.left.val)))
            if node.right:
                temp.append((node.right,path+"->"+str(node.right.val)))
            
        return res
