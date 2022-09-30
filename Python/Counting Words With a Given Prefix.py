from typing import List


class Solution:
    """
    Time:   O(n*k)
    Memory: O(1)

    where k - prefix length
    """

    def prefixCount(self, words: List[str], prefix: str) -> int:
        return sum(w.startswith(prefix) for w in words)
