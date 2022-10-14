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

    def deleteMiddle(self, head: ListNode) -> Optional[ListNode]:
        if head.next is None:
            return None

        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return head
