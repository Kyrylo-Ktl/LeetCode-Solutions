from typing import List


class Solution:
    """
    Time:   O(n^3)
    Memory: O(1)
    """

    SIZE = 3
    EMPTY = '.'

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(self.SIZE ** 2):
            for j in range(self.SIZE ** 2):
                if board[i][j] == self.EMPTY:
                    continue

                for k in range(self.SIZE ** 2):
                    if board[i][k] == board[i][j] and k != j:
                        return False
                    if board[k][j] == board[i][j] and k != i:
                        return False

                row = i - i % self.SIZE
                col = j - j % self.SIZE
                for r in range(row, row + self.SIZE):
                    for c in range(col, col + self.SIZE):
                        if board[r][c] == board[i][j] and (r != i or c != j):
                            return False

        return True


class Solution:
    """
    Time:   O(n^2)
    Memory: O(n^2)
    """

    SIZE = 3
    EMPTY = '.'

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = (
            [(val, r), (c, val), (r // self.SIZE, c // self.SIZE, val)]
            for r, row in enumerate(board)
            for c, val in enumerate(row)
            if val != self.EMPTY
        )
        seen = sum(seen, [])
        return len(seen) == len(set(seen))
