class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    def deleteNode(self, node: ListNode):
        node.val = node.next.val
        node.next = node.next.next
