class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def repeatedCharacter(self, s: str) -> str:
        seen = set()

        for c in s:
            if c in seen:
                return c
            seen.add(c)
