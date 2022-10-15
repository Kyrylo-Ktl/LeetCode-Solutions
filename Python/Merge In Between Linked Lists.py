class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Time:   O(n+m)
    Memory: O(1)
    """

    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start, end = None, list1

        for i in range(b):
            if i == a - 1:
                start = end
            end = end.next

        start.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = end.next

        return list1
