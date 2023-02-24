""" You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

________________

speed
O(N)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def valueSelector(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Tuple[Union[None, int], Union[Optional[ListNode], None], Union[Optional[ListNode], None]]:
        if not list1 and not list2:
            return None, None, None
        elif list1 and not list2:
            return list1.val, list1.next, None
        elif not list1 and list2:
            return list2.val, None, list2.next
        else:
            return {
                True: (list1.val, list1.next, list2),
                False: (list2.val, list1, list2.next)
            }.get(list1.val <= list2.val)

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode()
        curr_state = new_list

        while list1 or list2:
            
            val, list1, list2 = self.valueSelector(list1, list2)
            curr_state.next = ListNode(val)
            curr_state = curr_state.next

        return new_list.next
        

list1 = ListNode(1, ListNode(2, ListNode(4, None)))    
list2 = ListNode(1, ListNode(3, ListNode(4, None)))   
print(Solution.mergeTwoLists(list1, list2))
