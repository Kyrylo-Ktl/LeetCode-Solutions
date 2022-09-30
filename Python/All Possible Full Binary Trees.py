from functools import lru_cache
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time:   O(2^n)
    Memory: O(2^n)
    """

    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        return self._generate(n)

    @classmethod
    @lru_cache(None)
    def _generate(cls, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        if n == 1:
            return [TreeNode()]
        return [
            TreeNode(left=left, right=right)
            for x in range(n)
            for left in cls._generate(x)
            for right in cls._generate(n - 1 - x)
        ]
