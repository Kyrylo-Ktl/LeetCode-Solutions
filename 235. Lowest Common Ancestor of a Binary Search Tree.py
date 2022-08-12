class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < q.val:
            return self.lca(root, p, q)
        else:
            return self.lca(root, q, p)

    @classmethod
    def lca(cls, tree: TreeNode, lower: TreeNode, higher: TreeNode) -> TreeNode:
        if tree.val == lower.val or tree.val == higher.val:
            return tree

        if lower.val < tree.val < higher.val:
            return tree

        if higher.val < tree.val:
            return cls.lca(tree.left, lower, higher)
        else:
            return cls.lca(tree.right, lower, higher)
