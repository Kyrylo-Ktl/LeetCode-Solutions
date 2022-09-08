from typing import List


class Solution:
    """
    Time:   O(n*m)
    Memory: O(n*m)
    """

    WATER = 0
    LAND = 1

    def numEnclaves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        for i in range(n):
            self.sink_island(i, 0, grid)
            self.sink_island(i, m - 1, grid)

        for j in range(m):
            self.sink_island(0, j, grid)
            self.sink_island(n - 1, j, grid)

        return sum(map(sum, grid))

    @classmethod
    def sink_island(cls, row: int, col: int, grid: List[List[int]]):
        if grid[row][col] == cls.LAND:
            grid[row][col] = cls.WATER
            if row > 0:
                cls.sink_island(row - 1, col, grid)
            if row < len(grid) - 1:
                cls.sink_island(row + 1, col, grid)
            if col < len(grid[0]) - 1:
                cls.sink_island(row, col + 1, grid)
            if col > 0:
                cls.sink_island(row, col - 1, grid)
