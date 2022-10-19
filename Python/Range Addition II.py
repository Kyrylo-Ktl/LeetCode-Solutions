from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def maxCount(self, rows: int, cols: int, ops: List[List[int]]) -> int:
        if not ops:
            return rows * cols

        x, y = zip(*ops)
        return min(x) * min(y)


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def maxCount(self, rows: int, cols: int, ops: List[List[int]]) -> int:
        min_row = rows
        min_col = cols

        for row, col in ops:
            min_row = min(row, min_row)
            min_col = min(col, min_col)

        return min_row * min_col
