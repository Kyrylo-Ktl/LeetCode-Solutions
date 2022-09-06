from collections import defaultdict, deque
from typing import Generator, List, Optional


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def levelOrder(self, root: Optional[Node]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque([root])
        levels = []

        while queue:
            levels.append([])
            for _ in range(len(queue)):
                node = queue.popleft()
                levels[-1].append(node.val)
                queue.extend(node.children)

        return levels


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def levelOrder(self, root: Optional[Node]) -> List[List[int]]:
        levels = defaultdict(list)

        for node, depth in self._walk(root):
            levels[node].append(node.val)

        return [levels[d] for d in sorted(levels)]

    @classmethod
    def _walk(cls, root: Optional[Node], depth: int = 0) -> Generator:
        if root is None:
            return

        yield root, depth
        for child in root.children:
            yield from cls._walk(child, depth + 1)
