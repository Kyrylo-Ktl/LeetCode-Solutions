from typing import List


class Solution:
    """
    Time:   O(n^2)
    Memory: O(1)
    """

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        return [[self.local_max(grid, r, c, 1) for c in range(1, n - 1)] for r in range(1, n - 1)]

    @staticmethod
    def local_max(grid: List[List[int]], row: int, col: int, radius: int) -> int:
        return max(
            grid[r][c]
            for r in range(row - radius, row + radius + 1)
            for c in range(col - radius, col + radius + 1)
        )
