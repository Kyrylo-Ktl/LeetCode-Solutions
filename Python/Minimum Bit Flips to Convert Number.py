class Solution:
    """
    Time:   O(log(n))
    Memory: O(1)
    """

    def minBitFlips(self, start: int, goal: int) -> int:
        return (start ^ goal).bit_count()
