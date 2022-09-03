from typing import Generator, List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def allPathsSourceTarget(self, graph: List[List[int]]) -> Generator:
        def dfs(u: int, t: int, path: List[int]) -> Generator:
            if u == t:
                yield path

            for v in graph[u]:
                yield from dfs(v, t, path + [v])

        graph = {
            u: set(neighbours)
            for u, neighbours in enumerate(graph)
        }
        return dfs(0, len(graph) - 1, [0])
