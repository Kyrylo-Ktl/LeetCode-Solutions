from collections import Counter


class Solution:
    """
    Time:   O(n+m)
    Memory: O(n+m)
    """

    def canConstruct(self, ransom_note: str, magazine: str) -> bool:
        return not Counter(ransom_note) - Counter(magazine)
