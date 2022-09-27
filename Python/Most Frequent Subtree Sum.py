from collections import defaultdict
from typing import Optional, List


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

    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        count = defaultdict(int)
        self.dfs(root, count)
        max_count = max(count.values())
        return [s for s in count if count[s] == max_count]

    @classmethod
    def dfs(cls, root: Optional[TreeNode], count: defaultdict) -> int:
        if root is None:
            return 0

        s = root.val + cls.dfs(root.left, count) + cls.dfs(root.right, count)
        count[s] += 1
        return s
