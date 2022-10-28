from sys import maxsize
from typing import List


class Solution:
    """
    Time:   O(n^3)
    Memory: O(n^2)
    """

    def findTheCity(self, n: int, edges: List[List[int]], distance_threshold: int) -> int:
        dist = [[maxsize] * n for _ in range(n)]

        for u, v, w in edges:
            dist[u][v] = dist[v][u] = w

        for i in range(n):
            dist[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])

        min_city = min_neighbours = maxsize
        for i in range(n):
            neighbours = sum(dist[i][j] <= distance_threshold for j in range(n))
            if neighbours <= min_neighbours:
                min_city = i
                min_neighbours = neighbours

        return min_city
