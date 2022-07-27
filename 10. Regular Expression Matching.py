from functools import lru_cache


class Solution:
    """
    Time:   O(n*m)
    Memory: O(n*m)
    """
    ANY_SINGLE = '.'
    ZERO_OR_MORE_PREV = '*'

    def isMatch(self, string: str, pattern: str) -> bool:
        is_empty = lambda i: i < 0

        @lru_cache(maxsize=None)
        def dp(p: int, s: int) -> bool:
            if is_empty(p) and is_empty(s):
                return True

            if is_empty(p) or (is_empty(s) and pattern[p] != self.ZERO_OR_MORE_PREV):
                return False

            if pattern[p] == self.ANY_SINGLE or pattern[p] == string[s]:
                return dp(p - 1, s - 1)

            if pattern[p] == self.ZERO_OR_MORE_PREV:
                prev = pattern[p - 1]

                if not is_empty(s) and (string[s] == prev or prev == self.ANY_SINGLE):
                    return dp(p - 1, s) or dp(p, s - 1) or dp(p - 2, s)

                return dp(p - 2, s)

            return False

        return dp(len(pattern) - 1, len(string) - 1)
