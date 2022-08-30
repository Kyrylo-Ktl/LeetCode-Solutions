from typing import List


class Solution:
    """
    Time:   O(n^2)
    Memory: O(1)
    """

    def rotate(self, mat: List[List[int]]) -> None:
        n = len(mat)
        for layer in range(n // 2):
            for i in range((n + 1) // 2):
                mat[layer][i], mat[i][n - layer - 1], mat[n - layer - 1][n - i - 1], mat[n - i - 1][layer] = \
                mat[n - i - 1][layer], mat[layer][i], mat[i][n - layer - 1], mat[n - layer - 1][n - i - 1]
