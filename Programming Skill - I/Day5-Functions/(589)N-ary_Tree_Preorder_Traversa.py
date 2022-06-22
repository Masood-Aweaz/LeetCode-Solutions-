
'''********************************************************************************** 
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

 
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
**********************************************************************************'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    def preOrderHelper(self,root,visited):
        if root is None:
            return 
        visited.append(root.val)
        
        for i in root.children:
            self.preOrderHelper(i,visited)
    
    def preorder(self, root: 'Node') -> List[int]:
        visited = []
        if root is None:
            return visited 
        self.preOrderHelper(root,visited)
        return visited
