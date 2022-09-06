from functools import lru_cache
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time:   O(n^2)
    Memory: O(log(n))
    """

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self._generate(1, n)

    @classmethod
    @lru_cache(None)
    def _generate(cls, lo: int, hi: int) -> list:
        if lo > hi:
            return [None]
        return [
            TreeNode(root, left, right)
            for root in range(lo, hi + 1)  # All possible roots for the current subarray
            for left in cls._generate(lo, root - 1)  # All possible trees to the left of the root element
            for right in cls._generate(root + 1, hi)  # All possible trees to the right of the root element
        ]
