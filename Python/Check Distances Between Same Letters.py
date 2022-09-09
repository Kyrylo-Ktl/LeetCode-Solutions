from collections import defaultdict
from typing import List


class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d = defaultdict(list)

        for i, ch in enumerate(s):
            d[ch].append(i)

        return all(j - i - 1 == distance[ord(ch) - 97] for ch, (i, j) in d.items())
