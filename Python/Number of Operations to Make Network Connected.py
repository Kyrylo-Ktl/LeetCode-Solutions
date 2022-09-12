from collections import defaultdict
from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def dfs(u: int):
            visited.add(u)
            for v in graph[u]:
                if v not in visited:
                    dfs(v)

        if len(connections) < n - 1:
            return -1

        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        components = 0
        for v in range(n):
            if v not in visited:
                dfs(v)
                components += 1

        return components - 1
