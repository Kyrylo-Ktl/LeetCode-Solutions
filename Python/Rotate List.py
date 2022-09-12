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

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        tail = head
        length = 1

        while tail.next:
            length += 1
            tail = tail.next

        tail.next = head
        k %= length

        for _ in range(length - k):
            tail = tail.next

        head, tail.next = tail.next, None
        return head
