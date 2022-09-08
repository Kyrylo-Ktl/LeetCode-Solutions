from collections import defaultdict
from typing import List


class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(n)

    where n - len(first) + len(second)
    """

    def mergeSimilarItems(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
        merged = defaultdict(int)

        for value, weight in first + second:
            merged[value] += weight

        return sorted(merged.items())
