'''********************************************************************************** 
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

 

Example 1:


Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
**********************************************************************************'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.lst = []
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            self.lst.append(node.val)
            inorder(node.right)
        inorder(root)
        print(self.lst)
        r = TreeNode(self.lst[0])
        tmp = r
        for i in self.lst[1:]:
            ex = TreeNode(i)
            tmp.right = ex
            tmp.left = None 
            tmp = ex
        return r
