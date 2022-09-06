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

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        return self.rangeSumBST(root.left, low, high) + \
               self.rangeSumBST(root.right, low, high) + \
               root.val * (low <= root.val <= high)
