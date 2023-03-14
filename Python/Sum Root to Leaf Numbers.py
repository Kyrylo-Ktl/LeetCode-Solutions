from typing import Iterable, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time:   O(n)
    Memory: O(h)
    """

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return sum(self._get_paths(root, path=0))

    @classmethod
    def _get_paths(cls, root: Optional[TreeNode], path: int) -> Iterable[int]:
        if root is None:
            return

        path = path * 10 + root.val
        if root.left is None and root.right is None:
            yield path
        else:
            yield from cls._get_paths(root.left, path)
            yield from cls._get_paths(root.right, path)
