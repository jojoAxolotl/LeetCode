# 2095. Delete the Middle Node of a Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
from typing import ListNode

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle cases for a single node
        if head.next is None:
            return None
        
        # Initialize two pointers
        slow = head
        fast = head.next.next  # Start fast two steps ahead to ensure slow is one step behind the middle
        
        # Move fast pointer twice as fast as slow pointer
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        # Delete the middle node
        slow.next = slow.next.next
        
        return head