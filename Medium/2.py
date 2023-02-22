
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_l = ListNode()
        curr_state = new_l
        decade = 0
        while l1 or l2 or decade:
            val = decade
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            curr_state.next = ListNode(val % 10)
            decade = val // 10
            curr_state = curr_state.next

        return new_l.next
        