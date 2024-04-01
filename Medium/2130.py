# 2130. Maximum Twin Sum of a Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import copy
from typing import Optional
from typing import ListNode

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        sll = copy.deepcopy(head)
        def reverseList(head: Optional[ListNode]):
            cur = head
            result = None

            while cur:
                next_node = cur.next
                cur.next = result
                result = cur
                cur = next_node      
            return result
        
        reversedsll = reverseList(head)

        cur1 = sll
        cur2 = reversedsll
        maxtwin = 0

        while cur1:
            tmp = cur1.val + cur2.val
            if maxtwin < tmp:
                maxtwin = tmp
            cur1 = cur1.next
            cur2 = cur2.next

        return maxtwin