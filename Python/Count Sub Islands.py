from typing import List


class Solution:
    """
    Time:   O(n^2)
    Memory: O(n^2)
    """

    LAND = 1
    WATER = 0

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == self.LAND and grid1[i][j] == self.WATER:
                    self.sink_island(i, j, grid2)

        islands = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == self.LAND:
                    self.sink_island(i, j, grid2)
                    islands += 1

        return islands

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
