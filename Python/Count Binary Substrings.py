class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def countBinarySubstrings(self, s: str) -> int:
        substrings = 0
        prev, curr = 0, 1

        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                substrings += min(prev, curr)
                prev, curr = curr, 1
            else:
                curr += 1

        return substrings + min(prev, curr)
