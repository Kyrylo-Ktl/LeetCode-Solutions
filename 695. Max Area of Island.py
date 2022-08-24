from typing import List


class Solution:
    """
    Time:   O(n^2)
    Memory: O(1)
    """

    WATER = 0
    LAND = 1

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        return max(self.island_area(i, j, grid) for i in range(n) for j in range(m))

    @classmethod
    def island_area(cls, row: int, col: int, grid: List[List[int]]) -> int:
        if grid[row][col] != cls.LAND:
            return 0

        grid[row][col] = cls.WATER
        area = 1

        if row > 0:
            area += cls.island_area(row - 1, col, grid)

        if row + 1 < len(grid):
            area += cls.island_area(row + 1, col, grid)

        if col > 0:
            area += cls.island_area(row, col - 1, grid)

        if col + 1 < len(grid[0]):
            area += cls.island_area(row, col + 1, grid)

        return area
