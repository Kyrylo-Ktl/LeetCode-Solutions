from typing import List


class Solution:
    """
    Time:   O(V + E)
    Memory: O(V)
    """

    WHITE = 0
    GRAY = 1
    BLACK = 2

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(u: int) -> bool:
            if color[u] == self.GRAY:
                return True

            if color[u] == self.BLACK:
                return False

            color[u] = self.GRAY
            for v in graph[u]:
                if dfs(v):
                    return True

            color[u] = self.BLACK
            return False

        color = [self.WHITE] * len(graph)
        return [node for node in range(len(graph)) if not dfs(node)]
