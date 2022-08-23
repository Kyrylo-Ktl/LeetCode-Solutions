class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def secondsToRemoveOccurrences(self, s: str) -> int:
        seconds = zeros = 0

        for c in s:
            zeros += c == '0'
            if c == '1' and zeros > 0:
                seconds = max(seconds + 1, zeros)

        return seconds
