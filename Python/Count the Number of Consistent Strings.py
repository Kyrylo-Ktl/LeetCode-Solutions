from typing import List


class Solution:
    """
    Time:   O(n+m)
    Memory: O(n+m)

    where m - maximum word length
    """

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        return sum(not set(other) - allowed for other in words)
