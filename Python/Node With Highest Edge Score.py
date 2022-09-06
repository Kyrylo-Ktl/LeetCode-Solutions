from collections import defaultdict
from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def edgeScore(self, edges: List[int]) -> int:
        score = defaultdict(int)

        for u, v in enumerate(edges):
            score[v] += u

        return max(score, key=lambda x: (score[x], -x))
