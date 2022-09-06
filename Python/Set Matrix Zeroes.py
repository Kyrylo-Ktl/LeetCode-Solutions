from typing import List


class Solution:
    """
    Time:   O(n*m)
    Memory: O(n+m)
    """

    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])

        cols_to_set_zero = set()
        rows_to_set_zero = set()

        for row in range(n):
            for col in range(m):
                if matrix[row][col] == 0:
                    rows_to_set_zero.add(row)
                    cols_to_set_zero.add(col)

        for row in range(n):
            for col in range(m):
                if row in rows_to_set_zero or col in cols_to_set_zero:
                    matrix[row][col] = 0
