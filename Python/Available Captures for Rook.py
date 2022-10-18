from typing import List, Tuple


class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    SIZE = 8
    TURNS = [
        (-1, 0), (0, -1),
        ( 1, 0), (0,  1),
    ]
    PAWN = 'p'
    EMPTY = '.'
    ROOK = 'R'

    def numRookCaptures(self, board: List[List[str]]) -> int:
        num = 0
        start_x, start_y = self.get_rook_position(board)

        for dx, dy in self.TURNS:
            x, y = start_x, start_y
            while 0 <= x + dx < self.SIZE and 0 <= y + dy < self.SIZE:
                x += dx
                y += dy
                if board[x][y] != self.EMPTY:
                    num += board[x][y] == self.PAWN
                    break

        return num

    @classmethod
    def get_rook_position(cls, board: List[List[str]]) -> Tuple[int, int]:
        for x in range(cls.SIZE):
            for y in range(cls.SIZE):
                if board[x][y] == cls.ROOK:
                    return x, y
