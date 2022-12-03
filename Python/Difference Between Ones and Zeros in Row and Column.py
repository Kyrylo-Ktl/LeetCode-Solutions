from typing import List


class Solution:
    """
    Time:   O(n*m)
    Memory: O(n+m)
    """

    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])

        rows = [0] * n
        cols = [0] * m

        for i in range(n):
            for j in range(m):
                rows[i] += 1 if grid[i][j] else -1
                cols[j] += 1 if grid[i][j] else -1

        for i in range(n):
            for j in range(m):
                grid[i][j] = rows[i] + cols[j]

        return grid
