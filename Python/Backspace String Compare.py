from itertools import zip_longest
from typing import Generator


class Solution:
    """
    Time:   O(min(n, m))
    Memory: O(1)
    """

    def backspaceCompare(self, s: str, t: str) -> bool:
        return not any(a != b for a, b in zip_longest(self._build(s), self._build(t)))

    @staticmethod
    def _build(string: str) -> Generator:
        skip = 0
        for ch in reversed(string):
            if ch == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield ch
