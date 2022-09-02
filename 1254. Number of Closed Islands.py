from typing import List


class Solution:
    """
    Time:   O(n^2)
    Memory: O(n^2)
    """

    LAND = 0
    WATER = 1

    def closedIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        for row in range(n):
            self.water_island(row,     0, grid)
            self.water_island(row, m - 1, grid)

        for col in range(m):
            self.water_island(    0, col, grid)
            self.water_island(n - 1, col, grid)

        closed = 0
        for row in range(1, n - 1):
            for col in range(1, m - 1):
                if grid[row][col] == self.LAND:
                    self.water_island(row, col, grid)
                    closed += 1

        return closed

    @classmethod
    def water_island(cls, row: int, col: int, grid: List[List[int]]):
        if cls.in_bounds(row, col, grid) and grid[row][col] == cls.LAND:
            grid[row][col] = cls.WATER
            cls.water_island(row - 1, col, grid)
            cls.water_island(row + 1, col, grid)
            cls.water_island(row, col - 1, grid)
            cls.water_island(row, col + 1, grid)

    @staticmethod
    def in_bounds(row: int, col: int, grid: List[List[int]]) -> bool:
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])
