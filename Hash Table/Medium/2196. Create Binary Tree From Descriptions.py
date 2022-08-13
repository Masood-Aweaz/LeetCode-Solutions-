'''********************************************************************************** 
You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid.

 

Example 1:


Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]
Explanation: The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.
**********************************************************************************'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        dp = dict()
        for i in descriptions:
            if i[0] not in dp:
                dp[i[0]]=TreeNode(i[0])
            if i[1] not in dp:
                dp[i[1]]=TreeNode(i[1])
       # print(dp)
        
        parent = dict()
        for p,c,l in descriptions:
            parent[c]=True
            if l:
                dp[p].left = dp[c]
            else:
                dp[p].right = dp[c]
        
        #print(parent)
        #print(dp.keys())
        
        root = None
        for x in dp.keys():
            if x not in parent:
                root = dp[x]
        return root
        
        
        
