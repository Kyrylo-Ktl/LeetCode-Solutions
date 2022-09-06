from typing import List, Set, Tuple


class Solution:
    """
    Time:   O(n*m)
    Memory: O(n*m)
    """

    MOVES = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def pacificAtlantic(self, heights: List[List[int]]) -> Set[Tuple[int, int]]:
        def dfs(i: int, j: int, visited: set):
            visited.add((i, j))
            for di, dj in self.MOVES:
                x, y = i + di, j + dj
                if 0 <= x < n and 0 <= y < m and (x, y) not in visited and heights[i][j] <= heights[x][y]:
                    dfs(x, y, visited)

        n, m = len(heights), len(heights[0])

        atl_visited = set()
        pas_visited = set()

        for i in range(n):
            dfs(i,     0, atl_visited)
            dfs(i, m - 1, pas_visited)

        for j in range(m):
            dfs(    0, j, atl_visited)
            dfs(n - 1, j, pas_visited)

        return atl_visited & pas_visited
