from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    TYPES = 'PGM'

    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        last = {c: i for i, grb in enumerate(garbage) for c in grb}

        for i in range(1, len(travel)):
            travel[i] += travel[i - 1]

        return sum(map(len, garbage)) + sum(travel[i - 1] if i > 0 else 0 for c, i in last.items())
