from typing import List


class Solution:
    """
    Time:   O(n*m)
    Memory: O(n*m)
    """

    def findLength(self, a: List[int], b: List[int]) -> int:
        n, m = len(a), len(b)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                if a[i] == b[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1

        return max(map(max, dp))
