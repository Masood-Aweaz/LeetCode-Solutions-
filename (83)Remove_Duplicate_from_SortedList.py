'''********************************************************************************** 
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Input: head = [1,1,2]
Output: [1,2]
**********************************************************************************'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        temp = head
        while(temp != None):
            #print(temp.val)
            if temp.val not in res:
                res.append(temp.val)
                prev = temp
            elif temp.val in res:
                prev.next = temp.next
            
            temp = temp.next
        print(res)
        return head
        
