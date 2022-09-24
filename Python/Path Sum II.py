from typing import List, Optional, Generator


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], target_sum: int) -> Generator:
        return self.dfs(root, [], target_sum)

    @classmethod
    def dfs(cls, tree: Optional[TreeNode], cur_path: List[int], target: int) -> Generator:
        if tree is None:
            return None

        cur_path.append(tree.val)
        target -= tree.val
        if cls.is_leaf(tree) and not target:
            yield cur_path
        else:
            yield from cls.dfs( tree.left, cur_path[:], target)
            yield from cls.dfs(tree.right, cur_path[:], target)

    @classmethod
    def is_leaf(cls, node: TreeNode) -> bool:
        return node.left is None and node.right is None
