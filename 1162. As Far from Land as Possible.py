from sys import maxsize
from typing import List


class Solution:
    """
    Time:   O(n*m)
    Memory: O(n*m)
    """

    def maxDistance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dist = [[0 if grid[i][j] else maxsize for j in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                if i > 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j > 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)

        for i in reversed(range(n)):
            for j in reversed(range(m)):
                if i < n - 1:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j < m - 1:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)

        max_dist = max(map(max, dist))
        return -1 if max_dist in (0, maxsize) else max_dist
