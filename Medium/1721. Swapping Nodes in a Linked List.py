'''********************************************************************************** 
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
**********************************************************************************'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodeStart = head
        kStart = k
        
        #find the kth node from the beginning
        while kStart - 1 > 0:
            nodeStart = nodeStart.next
            kStart -= 1
        
        #initialize the fast pointer for the iteration
        nodeEnd, fast = head, head
        while k - 1 > 0:
            fast = fast.next
            k -= 1
        
        #find the kth node from the end
        while fast and fast.next:
            nodeEnd = nodeEnd.next
            fast = fast.next
        
        #swap values
        nodeStart.val, nodeEnd.val = nodeEnd.val, nodeStart.val
        
        return head
            
        
