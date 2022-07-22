'''********************************************************************************** 
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
**********************************************************************************'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)
        
        while head:
            if head.val< x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
            
        after.next = None
        before.next = after_head.next
        
        return before_head.next
