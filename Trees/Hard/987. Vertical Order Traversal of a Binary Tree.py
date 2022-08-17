'''********************************************************************************** 
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.
**********************************************************************************'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def order(root,hd,m,level):
            if not root:
                return 
            if m.get(hd):
                if m[hd].get(level):
                    m[hd][level].append(root.val)
                else:
                    m[hd][level]=[root.val]
            else:
                m[hd]={level:[root.val]}
            order(root.left,hd-1,m,level+1)
            order(root.right,hd+1,m,level+1)
            
        m = dict()
        hd = 0
        order(root,hd,m,1)
        print(m)
        
        tmp = sorted(m.keys())
        
        print(tmp)
        res=[]
        for i in tmp:
            temp = []
            for l in sorted(m[i]):
                temp+=sorted(m[i][l])
            res.append(temp)
        return res
        
