from typing import Optional, Tuple


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

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter, _ = self._get_diameter(root)
        return diameter

    @classmethod
    def _get_diameter(cls, tree: Optional[TreeNode]) -> Tuple[int, int]:
        if tree is None:
            return 0, 0

        left_diam, left_path = cls._get_diameter(tree.left)
        right_diam, right_path = cls._get_diameter(tree.right)

        return max(left_path + right_path, left_diam, right_diam), max(left_path, right_path) + 1
