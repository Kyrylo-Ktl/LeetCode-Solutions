from collections import Counter
from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def minimumRounds(self, tasks: List[int]) -> int:
        min_rounds = 0

        for cnt in Counter(tasks).values():
            if cnt == 1:
                return -1
            min_rounds += cnt // 3 + int(cnt % 3 != 0)

        return min_rounds
