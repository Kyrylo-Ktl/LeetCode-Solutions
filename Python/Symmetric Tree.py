from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def isSymmetric(self, root: TreeNode) -> bool:
        left_queue = deque([root.left])
        right_queue = deque([root.right])

        while right_queue and left_queue:
            left = left_queue.popleft()
            right = right_queue.popleft()

            if not left and not right:
                continue
            if (left and not right) or (not left and right):
                return False
            if left.val != right.val:
                return False

            left_queue.extend([left.right, left.left])
            right_queue.extend([right.left, right.right])

        return not left_queue and not right_queue


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def isSymmetric(self, root: TreeNode) -> bool:
        return self._is_symmetric(root.left, root.right)

    @classmethod
    def _is_symmetric(cls, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if (left and not right) or (not left and right):
            return False
        if left.val != right.val:
            return False
        return cls._is_symmetric(left.right, right.left) and \
               cls._is_symmetric(left.left, right.right)
