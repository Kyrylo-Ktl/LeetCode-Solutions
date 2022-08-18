from collections import Counter
from typing import List


class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(n)
    """

    def minSetSize(self, arr: List[int]) -> int:
        total_count = 0

        for index, count in enumerate(sorted(Counter(arr).values(), reverse=True)):
            total_count += count
            if total_count >= len(arr) // 2:
                return index + 1

        return 0
