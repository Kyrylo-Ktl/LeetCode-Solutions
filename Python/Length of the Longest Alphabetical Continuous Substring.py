class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def longestContinuousSubstring(self, s: str) -> int:
        longest = current = 0
        prev = '*'

        for c in s:
            if ord(prev) + 1 != ord(c):
                current = 1
            else:
                current += 1

            prev = c
            longest = max(longest, current)

        return longest
