from typing import List


class NumMatrix:
    """
    Time:
        creation - O(n*m)
        query    - O(1)
    Memory:
        creation - O(n*m)
        query    - O(1)
    """

    def __init__(self, matrix: List[List[int]]):
        n, m = len(matrix), len(matrix[0])
        self.dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                self.dp[i][j] = self.dp[i][j - 1] + self.dp[i - 1][j] + matrix[i - 1][j - 1] - self.dp[i - 1][j - 1]

    def sumRegion(self, start_row: int, start_col: int, end_row: int, end_col: int) -> int:
        return self.dp[end_row + 1][end_col + 1] + self.dp[start_row][start_col] - \
               self.dp[start_row][end_col + 1] - self.dp[end_row + 1][start_col]
