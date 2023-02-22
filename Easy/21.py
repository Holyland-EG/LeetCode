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
        