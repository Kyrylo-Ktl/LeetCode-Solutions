from collections import deque
from typing import Generator, List


class Solution:
    """
    Time:   O(n^2)
    Memory: O(n^2)
    """

    NEIGHBOURS = (
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
    )

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        queue = deque([(0, 0)])
        seen = {(0, 0)}
        n = len(grid)

        steps = 0
        while queue:
            steps += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if x == n - 1 and y == n - 1:
                    return steps
                for next_x, next_y in self.get_neighbours(x, y, n):
                    if (next_x, next_y) not in seen and grid[next_x][next_y] != 1:
                        seen.add((next_x, next_y))
                        queue.append((next_x, next_y))

        return -1

    @classmethod
    def get_neighbours(cls, row: int, col: int, n: int) -> Generator:
        for dr, dc in cls.NEIGHBOURS:
            if 0 <= row + dr < n and 0 <= col + dc < n:
                yield row + dr, col + dc
