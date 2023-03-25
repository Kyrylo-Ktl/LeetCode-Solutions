from collections import defaultdict
from typing import List


class Solution:
    """
    Time:   O(V + E)
    Memory: O(V + E)
    """

    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def dfs(u: int, visited: set = set()) -> int:
            if u in visited:
                return 0
            visited.add(u)
            return 1 + sum(dfs(v) for v in graph[u])

        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        return sum(reached * (n - reached) for reached in map(dfs, range(n))) // 2
