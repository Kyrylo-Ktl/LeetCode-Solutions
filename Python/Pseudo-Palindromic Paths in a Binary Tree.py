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

    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        return self.preorder(root, path=0)

    @classmethod
    def preorder(cls, node: Optional[TreeNode], path: int) -> int:
        if node is None:
            return 0

        path = path ^ (1 << node.val)

        if node.left is None and node.right is None:
            return int(path & (path - 1) == 0)

        return cls.preorder(node.left, path) + cls.preorder(node.right, path)
