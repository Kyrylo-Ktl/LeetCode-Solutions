from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time:   O(n)
    Memory: O(H)
    """

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p is None and q is None
        return p.val == q.val \
            and self.isSameTree(p.left, q.left) \
            and self.isSameTree(p.right, q.right)
