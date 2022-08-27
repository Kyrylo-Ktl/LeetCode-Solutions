from sys import maxsize
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time:   O(n)
    Memory: O(log(n))
    """

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum, _ = self._max_path_sum(root)
        return max_sum

    def _max_path_sum(self, root: Optional[TreeNode]) -> tuple:
        if root is None:
            return -maxsize, 0

        left_max_sum, left_path_sum = self._max_path_sum(root.left)
        right_max_sum, right_path_sum = self._max_path_sum(root.right)

        return max(left_max_sum, right_max_sum, left_path_sum + root.val + right_path_sum), \
               max(root.val + max(left_path_sum, right_path_sum), 0)
