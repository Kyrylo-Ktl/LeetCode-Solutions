from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = result = ListNode()

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
            else:
                curr.next = ListNode(head.val)
                curr = curr.next
            head = head.next

        return result.next
