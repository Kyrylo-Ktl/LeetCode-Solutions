from itertools import zip_longest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time:   O(H)
    Memory: O(H)
    """

    def leafSimilar(self, first: Optional[TreeNode], second: Optional[TreeNode]) -> bool:
        return all(x == y for x, y in zip_longest(self._get_leaves(first), self._get_leaves(second)))

    @classmethod
    def _get_leaves(cls, tree: Optional[TreeNode]):
        if tree is not None:
            if cls.is_leaf(tree):
                yield tree.val
            yield from cls._get_leaves(tree.left)
            yield from cls._get_leaves(tree.right)

    @staticmethod
    def is_leaf(node: TreeNode) -> bool:
        return node.left is None and node.right is None
