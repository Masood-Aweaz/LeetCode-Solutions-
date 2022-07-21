'''********************************************************************************** 
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
**********************************************************************************'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    
       
        dummy = ListNode(0,head)
        
        #find the left node
        leftPrev = dummy
        curr = head
        
        for i in range(left-1):
            leftPrev = curr
            curr = curr.next
        
        #iterate till the prev points the right node (r-l+1)
        prev = None
        for i in range(right-left+1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        #update the pointers
        leftPrev.next.next = curr
        leftPrev.next = prev
        
        return dummy.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
