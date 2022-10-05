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

    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        return self._add_row(root, val, depth, is_left=True)

    @classmethod
    def _add_row(cls, tree: Optional[TreeNode], val: int, depth: int, is_left: bool) -> Optional[TreeNode]:
        if depth == 1 and is_left:
            return TreeNode(val=val, left=tree)

        if depth == 1 and not is_left:
            return TreeNode(val=val, right=tree)

        if tree is not None:
            tree.left = cls._add_row(tree.left, val, depth - 1, True)
            tree.right = cls._add_row(tree.right, val, depth - 1, False)

        return tree
