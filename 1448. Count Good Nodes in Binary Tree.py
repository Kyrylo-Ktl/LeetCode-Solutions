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

    def goodNodes(self, root: TreeNode) -> int:
        return self._good_nodes(root, -maxsize)

    @classmethod
    def _good_nodes(cls, node: Optional[TreeNode], curr_max: int) -> int:
        if node is None:
            return 0

        curr_max = max(curr_max, node.val)
        return (node.val >= curr_max) + \
               cls._good_nodes(node.left, curr_max) + \
               cls._good_nodes(node.right, curr_max)
