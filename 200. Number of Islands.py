from typing import List


class Solution:
    """
    Time:   O(n*m)
    Memory: O(n*m)
    """

    LAND = '1'
    WATER = '0'
    MOVES = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])

        islands = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == self.LAND:
                    self._visit(row, col, grid)
                    islands += 1

        return islands

    @classmethod
    def _visit(cls, row: int, col: int, grid: List[List[str]]):
        n, m = len(grid), len(grid[0])
        grid[row][col] = cls.WATER

        if row > 0 and grid[row - 1][col] == cls.LAND:
            cls._visit(row - 1, col, grid)
        if row + 1 < n and grid[row + 1][col] == cls.LAND:
            cls._visit(row + 1, col, grid)
        if col > 0 and grid[row][col - 1] == cls.LAND:
            cls._visit(row, col - 1, grid)
        if col + 1< m and grid[row][col + 1] == cls.LAND:
            cls._visit(row, col + 1, grid)
