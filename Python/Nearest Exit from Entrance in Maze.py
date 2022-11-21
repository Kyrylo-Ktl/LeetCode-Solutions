from collections import deque
from typing import List


class Solution:
    """
    Time:   O(n*m)
    Memory: O(n*m)
    """

    EMPTY = '.'
    WALL = '+'
    MOVES = (
        (-1, 0), (0, -1),
        ( 0, 1), (1,  0),
    )

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        start_row, start_col = entrance
        queue = deque([entrance])
        distance = 0

        while queue:
            distance += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in self.MOVES:
                    move_row, move_col = row + dr, col + dc
                    if self.in_bounds(move_row, move_col, maze) and maze[move_row][move_col] == self.EMPTY:
                        if self.at_border(move_row, move_col, maze) and \
                                (move_row != start_row or move_col != start_col):
                            return distance
                        maze[move_row][move_col] = self.WALL
                        queue.append([move_row, move_col])

        return -1

    @staticmethod
    def in_bounds(row: int, col: int, maze: List[List[str]]) -> bool:
        return 0 <= row < len(maze) and 0 <= col < len(maze[0])

    @staticmethod
    def at_border(row: int, col: int, maze: List[List[str]]) -> bool:
        return row == 0 or col == 0 or row + 1 == len(maze) or col + 1 == len(maze[0])
