from functools import lru_cache


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def numDecodings(self, s: str) -> int:
        @lru_cache(maxsize=None)
        def dp(i: int):
            if i < n and s[i] == '0':
                return 0
            if n - i < 2:
                return 1
            return dp(i + 1) + (int(s[i:i + 2]) <= 26) * dp(i + 2)

        n = len(s)
        return dp(0)
