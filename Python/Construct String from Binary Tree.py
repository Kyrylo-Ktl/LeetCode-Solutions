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

    def tree2str(self, root: TreeNode) -> str:
        return self._construct(root)

    @classmethod
    def _construct(cls, tree: Optional[TreeNode]) -> str:
        if tree is None:
            return ''

        return '{}{}{}'.format(
            tree.val,
            f'({cls._construct(tree.left)})' * (tree.left is not None or tree.right is not None),
            f'({cls._construct(tree.right)})' * (tree.right is not None),
        )
