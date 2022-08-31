from typing import Optional


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

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root is not None and root.val != val:
            root = root.left if val < root.val else root.right
        return root


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None or root.val == val:
            return root
        return self.searchBST(root.left if val < root.val else root.right, val)
