from functools import cache, reduce
from operator import or_
from typing import Generator, List


class Solution:
    POWERS = [
        0b000000000000000000001,
        0b000000000000000000010,
        0b000000000000000000100,
        0b000000000000000001000,
        0b000000000000000010000,
        0b000000000000000100000,
        0b000000000000001000000,
        0b000000000000010000000,
        0b000000000000100000000,
        0b000000000001000000000,
        0b000000000010000000000,
        0b000000000100000000000,
        0b000000001000000000000,
        0b000000010000000000000,
        0b000000100000000000000,
        0b000001000000000000000,
        0b000010000000000000000,
        0b000100000000000000000,
        0b001000000000000000000,
        0b010000000000000000000,
        0b100000000000000000000,
    ]

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        @cache
        def paths(i: int, j: int, mask: int) -> int:
            if grid[i][j] == 2 and mask == target_mask:
                return 1

            return sum(
                paths(ni, nj, mask | self.POWERS[ni * n + nj])
                for ni, nj in self.get_neighbours(i, j, grid)
                if not mask & self.POWERS[ni * n + nj]
            )

        m, n = len(grid), len(grid[0])
        target_mask = (1 << m * n) - 1

        return paths(
            *self.find_start(grid),
            mask=reduce(or_, (self.POWERS[i * n + j] for i in range(m) for j in range(n) if grid[i][j] in (-1, 1)))
        )

    @staticmethod
    def find_start(grid: List[List[int]]) -> tuple[int, int]:
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item == 1:
                    return i, j

    @staticmethod
    def get_neighbours(i: int, j: int, grid: List[List[int]]) -> Generator:
        n, m = len(grid), len(grid[0])

        for ni, nj in (i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j):
            if 0 <= ni < n and 0 <= nj < m:
                yield ni, nj
