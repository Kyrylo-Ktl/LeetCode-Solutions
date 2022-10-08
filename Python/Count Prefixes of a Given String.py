from typing import List


class Solution:
    """
    Time:   O(n*m)
    Memory: O(n*m)
    """

    def countPrefixes(self, words: List[str], s: str) -> int:
        return sum(map(s.startswith, words))
