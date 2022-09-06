from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Time:   O(n + m)
    Memory: O(1)
    """

    def addTwoNumbers(self, first: Optional[ListNode], second: Optional[ListNode]) -> Optional[ListNode]:
        root = temp = ListNode()
        carry = 0

        while first or second or carry:
            a = b = 0

            if first:
                a = first.val
                first = first.next

            if second:
                b = second.val
                second = second.next

            carry, val = divmod(a + b + carry, 10)
            temp.next = ListNode(val)
            temp = temp.next

        return root.next
