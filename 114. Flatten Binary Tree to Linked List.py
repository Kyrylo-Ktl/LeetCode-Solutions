from typing import Generator, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def flatten(self, root: Optional[TreeNode]) -> None:
        prev = None
        for node in self.preorder(root):
            node.left = None
            node.right, prev = prev, node

    @classmethod
    def preorder(cls, tree: Optional[TreeNode]) -> Generator:
        if tree is not None:
            yield from cls.preorder(tree.right)
            yield from cls.preorder(tree.left)
            yield tree
