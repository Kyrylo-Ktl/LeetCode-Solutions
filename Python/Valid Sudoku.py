from typing import List


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
