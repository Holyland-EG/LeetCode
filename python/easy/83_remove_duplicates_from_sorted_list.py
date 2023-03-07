""" Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.

________________

speed
O(N)
"""
from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode()
        curr = new_list
        unique_nums = set()

        while head:
            if head.val not in unique_nums:
                unique_nums.add(head.val)
                curr.next = ListNode(head.val)
                curr = curr.next
            head = head.next

        return new_list.next
        