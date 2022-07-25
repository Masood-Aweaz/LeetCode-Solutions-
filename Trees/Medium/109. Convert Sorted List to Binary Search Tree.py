'''********************************************************************************** 
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

 

Example 1:


Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
**********************************************************************************'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        tmp = []
        while(head):
            tmp.append(head.val)
            head = head.next
        #print(tmp)
        
        def help(l,r):
            if l>r:
                return None
            m = (l+r)//2
            root = TreeNode(tmp[m])
            root.left = help(l,m-1)
            root.right = help(m+1,r)
            return root
        return help(0,len(tmp)-1)
            
            
