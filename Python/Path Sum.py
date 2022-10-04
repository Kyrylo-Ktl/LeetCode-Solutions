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

    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return target == root.val
        return self.hasPathSum( root.left, target - root.val) or \
               self.hasPathSum(root.right, target - root.val)
