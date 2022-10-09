from typing import Generator, Optional


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

    def findTarget(self, root: TreeNode, k: int) -> bool:
        def dfs(tree: Optional[TreeNode]) -> bool:
            if tree is None:
                return False
            if k - tree.val in memo:
                return True
            memo.add(tree.val)
            return dfs(tree.left) or dfs(tree.right)

        memo = set()
        return dfs(root)


class Solution:
    """
    Time:   O(n)
    Memory: O(h)
    """

    def findTarget(self, root: TreeNode, k: int) -> bool:
        min_to_max_order = self.asc_traverse(root)
        left = next(min_to_max_order)

        max_to_min_order = self.desc_traverse(root)
        right = next(max_to_min_order)

        while left < right:
            if right + left == k:
                return True

            if right + left < k:
                left = next(min_to_max_order)
            else:
                right = next(max_to_min_order)

        return False

    @classmethod
    def asc_traverse(cls, tree: Optional[TreeNode]) -> Generator:
        if tree is not None:
            yield from cls.asc_traverse(tree.left)
            yield tree.val
            yield from cls.asc_traverse(tree.right)

    @classmethod
    def desc_traverse(cls, tree: Optional[TreeNode]) -> Generator:
        if tree is not None:
            yield from cls.desc_traverse(tree.right)
            yield tree.val
            yield from cls.desc_traverse(tree.left)
