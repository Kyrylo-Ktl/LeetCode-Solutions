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

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


class Solution:
    """
    Time:   O(log^2(n))
    Memory: O(log(n))
    """

    def countNodes(self, root: Optional[TreeNode], nodes: int = 0) -> int:
        if root is None:
            return nodes

        if root.left is None and root.right is None:
            return nodes + 1

        if self.height(root.left) == self.height(root.right):
            return self.countNodes(root.right, 2 * nodes + 2)
        return self.countNodes(root.left, 2 * nodes + 1)

    @classmethod
    def height(cls, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + cls.height(root.left)
