from typing import Generator


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

    def smallestFromLeaf(self, root: TreeNode) -> str:
        return min(self.dfs(root, string=''))

    @classmethod
    def dfs(cls, tree: TreeNode, string: str) -> Generator:
        string = chr(ord('a') + tree.val) + string

        if tree.left is None and tree.right is None:
            yield string
            return

        if tree.left is not None:
            yield from cls.dfs(tree.left, string)

        if tree.right is not None:
            yield from cls.dfs(tree.right, string)
