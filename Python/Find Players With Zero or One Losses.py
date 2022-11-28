from collections import defaultdict
from typing import List


class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(n)
    """

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loses = defaultdict(int)
        wins = defaultdict(int)

        for w, l in matches:
            loses[l] += 1
            wins[w] += 1

        return [
            sorted(w for w in wins if not loses[w]),
            sorted(l for l in loses if loses[l] == 1),
        ]
