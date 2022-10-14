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

    def maxAncestorDiff(self, root: TreeNode) -> int:
        _, _, diff = self.max_diff(root)
        return diff

    @classmethod
    def max_diff(cls, tree: TreeNode) -> tuple:
        l_min, l_max, l_diff = (tree.val, tree.val, 0) if tree.left is None else cls.max_diff(tree.left)
        r_min, r_max, r_diff = (tree.val, tree.val, 0) if tree.right is None else cls.max_diff(tree.right)

        c_min, c_max = min(l_min, r_min, tree.val), max(l_max, r_max, tree.val),
        c_diff = max(l_diff, r_diff, abs(tree.val - c_min), abs(tree.val - c_max))

        return c_min, c_max, c_diff
