'''********************************************************************************** 
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

 

Example 1:


Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
**********************************************************************************'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        visited = []
        queue = []
        
        def bfs(visited,node,queue):
            visited.append(node)
            queue.append(node)
            
            while queue:
                m = queue.pop(0)
                if m.val==val:
                    return m
                if m.left and m.left not in visited:
                    visited.append(m.left)
                    queue.append(m.left)
                if m.right and m.right not in visited:
                    visited.append(m.right)
                    queue.append(m.right)
            return None
        return bfs(visited,root,queue)
