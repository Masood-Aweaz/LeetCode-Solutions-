'''********************************************************************************** 
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
**********************************************************************************'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        temp=head
        prev=head
        while temp:
            if head.val==val:
                head=head.next
                temp=head
                prev=temp
            elif temp.val!=val:
                prev=temp
                temp=temp.next
            elif temp.val==val:
                prev.next=temp.next
                temp=temp.next
        return head
    
    
    
    
    
     
