from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []

        while head:
            vals += head.val,
            head = head.next

        return vals == vals[::-1]


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next

        return not rev
