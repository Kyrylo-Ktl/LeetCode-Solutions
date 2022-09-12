from collections import defaultdict
from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def dfs(curr: int, parent: int) -> int:
            return sum(cost + dfs(nei, curr) for nei, cost in graph[curr] if nei != parent)

        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))

        return dfs(0, -1)
