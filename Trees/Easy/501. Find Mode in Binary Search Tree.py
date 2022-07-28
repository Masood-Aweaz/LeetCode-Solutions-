'''********************************************************************************** 
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [1,null,2,2]
Output: [2]
**********************************************************************************'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = dict()
        def dfs(root,d):
            if not root:
                return d
            if root.val not in d.keys():
                d[root.val]=1
            else:
                d[root.val]+=1
            if root.left:
                dfs(root.left,d)
            if root.right:
                dfs(root.right,d)
            return d
        
        x=dfs(root,d)
        max_num = max(d.values())
        return [i for i,value in d.items() if(value==max_num)]
            
