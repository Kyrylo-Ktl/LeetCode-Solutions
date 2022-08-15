from collections import Counter
from typing import List


class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        max_rank_cnt = max(Counter(ranks).values())
        max_suit_cnt = max(Counter(suits).values())

        return {
            max_rank_cnt == 2: 'Pair',
            max_rank_cnt >= 3: 'Three of a Kind',
            max_suit_cnt == 5: 'Flush',
        }.get(True, 'High Card')
