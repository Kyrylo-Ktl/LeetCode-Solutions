from collections import Counter
from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(set(arr)) == len(set(Counter(arr).values()))
