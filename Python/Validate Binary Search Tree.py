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
    Memory: O(n)
    """

    INF = maxsize

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._validate(root, -self.INF, self.INF)

    @classmethod
    def _validate(cls, root: Optional[TreeNode], min_val: int, max_val: int) -> bool:
        if root is None:
            return True
        if root.val <= min_val or max_val <= root.val:
            return False
        return cls._validate( root.left,  min_val, root.val) and \
               cls._validate(root.right, root.val,  max_val)
