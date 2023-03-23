from collections import defaultdict
from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    WHITE = 0
    GRAY = 1
    BLACK = -1

    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i: int) -> bool:
            if color[i] == self.GRAY:
                return True
            if color[i] == self.BLACK:
                return False

            color[i] = self.GRAY
            for j in graph[i]:
                if dfs(j):
                    return True

            color[i] = self.BLACK
            return False

        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        color = [self.WHITE] * n
        return not any(map(dfs, range(n)))
