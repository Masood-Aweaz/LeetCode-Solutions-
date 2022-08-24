'''********************************************************************************** 
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

 

Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
**********************************************************************************'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.lst=[]
        def inorder(node):
            if not node:
                return 
            self.lst.append(node.val)
            inorder(node.left)
            inorder(node.right)
            
        inorder(root)
        print(self.lst)
        x=sorted(self.lst)
        if len(x)==1:
            return False
        print(x)
        for i in range(len(x)):
            print(k-x[i])
            if k-x[i] in x[i+1:]:
                return True
        return False
