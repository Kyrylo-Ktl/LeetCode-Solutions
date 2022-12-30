from typing import List


class Solution:
    """
    Time:   O(n*m)
    Memory: O(n*m)
    """

    EMPTY = 0
    VISITED = 1

    def regionsBySlashes(self, grid: List[str]) -> int:
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0 or i >= 3 * n or j >= 3 * m or g[i][j] != self.EMPTY:
                return 0
            g[i][j] = self.VISITED
            return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)

        n, m = len(grid), len(grid[0])
        g = [[self.EMPTY] * m * 3 for _ in range(n * 3)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '/':
                    g[i * 3][j * 3 + 2] = g[i * 3 + 1][j * 3 + 1] = g[i * 3 + 2][j * 3] = self.VISITED
                elif grid[i][j] == '\\':
                    g[i * 3][j * 3] = g[i * 3 + 1][j * 3 + 1] = g[i * 3 + 2][j * 3 + 2] = self.VISITED

        return sum(
            min(1, dfs(i, j))
            for i in range(n * 3)
            for j in range(m * 3)
        )
