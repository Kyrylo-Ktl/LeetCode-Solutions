from typing import List


class Solution:
    """
    Time:   O(n^2)
    Memory: O(n^2)
    """

    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        size = n * m
        return [[grid[(i * m + j - k) % size // m][(i * m + j - k) % size % m] for j in range(m)] for i in range(n)]
