'''********************************************************************************** 
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
**********************************************************************************'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        #print(p.val)
        dummy = head
        if  head==None:
            return head
        if head.next==None:
            return head
        while(p):
            if p.next==None:
                return dummy
            q=p.next
            #r=q.next
            tmp = p.val
            p.val = q.val
            q.val = tmp
            p = q.next
        return dummy
            
            
