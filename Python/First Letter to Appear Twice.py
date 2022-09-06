class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def repeatedCharacter(self, s: str) -> str:
        seen = set()

        for c in s:
            if c in seen:
                return c
            seen.add(c)
