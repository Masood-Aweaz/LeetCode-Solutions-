'''********************************************************************************** 
You are given the head of a linked list containing unique integer values and an integer array nums that is a subset of the linked list values.

Return the number of connected components in nums where two values are connected if they appear consecutively in the linked list.

 

Example 1:


Input: head = [0,1,2,3], nums = [0,1,3]
Output: 2
Explanation: 0 and 1 are connected, so [0, 1] and [3] are the two connected components.
**********************************************************************************'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        curr = head
        prev = None
        c=0
        '''while curr.next:
            prev = curr
            curr = curr.next
            if (prev.val in nums and curr.val in nums):
                c+=1
                nums.remove(prev.val)
                nums.remove(curr.val)
        if nums:
            c+=len(nums)
        return c'''
        seen = set(nums)
        while curr:
            if curr.val in seen and prev not in seen:
                c+=1
            prev = curr.val
            curr = curr.next
        return c
