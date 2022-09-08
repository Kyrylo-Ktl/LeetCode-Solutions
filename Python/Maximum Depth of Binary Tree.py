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

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return max(
            self.maxDepth(root.left),
            self.maxDepth(root.right),
        ) + 1 if root is not None else 0
