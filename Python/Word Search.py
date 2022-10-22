from typing import List


class Solution:
    """
    Time:   O(n*m*k)
    Memory: O(k)

    where k - word length
    """

    VISITED = '#'

    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])

        beginning = end = 0
        for r in range(n):
            for c in range(m):
                if board[r][c] == word[0]:
                    beginning += 1
                elif board[r][c] == word[-1]:
                    end += 1

        if beginning > end:
            word = word[::-1]

        for i in range(n):
            for j in range(m):
                if self.dfs(board, i, j, 0, word):
                    return True

        return False

    @classmethod
    def dfs(cls, board: List[List[str]], i: int, j: int, k: int, word: str) -> bool:
        if k == len(word):
            return True

        n, m = len(board), len(board[0])
        if (i < 0 or i >= n) or (j < 0 or j >= m) or word[k] != board[i][j]:
            return False

        board[i][j] = cls.VISITED
        res = cls.dfs(board, i + 1, j, k + 1, word) or \
              cls.dfs(board, i - 1, j, k + 1, word) or \
              cls.dfs(board, i, j + 1, k + 1, word) or \
              cls.dfs(board, i, j - 1, k + 1, word)
        board[i][j] = word[k]

        return res
