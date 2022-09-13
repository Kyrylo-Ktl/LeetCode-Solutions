from typing import List


class Solution:
    """
    Time:   O(n*m)
    Memory: O(1)
    """

    LAND = 1
    WATER = 0

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        perimeter = 0

        for r in range(n):
            for c in range(m):
                if grid[r][c] != self.LAND:
                    continue
                if r == 0     or grid[r - 1][c] == self.WATER:
                    perimeter += 1
                if r == n - 1 or grid[r + 1][c] == self.WATER:
                    perimeter += 1
                if c == 0     or grid[r][c - 1] == self.WATER:
                    perimeter += 1
                if c + 1 == m or grid[r][c + 1] == self.WATER:
                    perimeter += 1

        return perimeter


class Solution:
    """
    Time:   O(n*m)
    Memory: O(1)
    """

    LAND = 1
    WATER = 0

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        return sum(
            sum([
                r == 0     or grid[r - 1][c] == self.WATER,
                r == n - 1 or grid[r + 1][c] == self.WATER,
                c == 0     or grid[r][c - 1] == self.WATER,
                c + 1 == m or grid[r][c + 1] == self.WATER
            ]) for r in range(n)
            for c in range(m) if grid[r][c] == self.LAND
        )
