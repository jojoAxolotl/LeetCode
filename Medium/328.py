# 328. Odd Even Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from typing import ListNode

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head
        ll2head = head.next
        cur = head
        odd = True
        while cur.next.next:
            tmp = cur.next
            cur.next = cur.next.next
            cur = tmp
            odd = not odd
        
        # print(head) # odd 
        # print(cur) # last three
        # print(ll2head) # even 

        if odd:
            cur.next = ll2head
        else:
            tmp = cur.next
            cur.next = None
            tmp.next  = ll2head
        return head