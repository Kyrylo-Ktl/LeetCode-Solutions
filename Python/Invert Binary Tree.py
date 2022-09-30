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

    def invertTree(self, tree: Optional[TreeNode]) -> Optional[TreeNode]:
        if tree is not None:
            tree.left, tree.right = self.invertTree(tree.right), self.invertTree(tree.left)
        return tree
