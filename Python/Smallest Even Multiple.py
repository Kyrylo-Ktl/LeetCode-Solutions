class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    def smallestEvenMultiple(self, n: int) -> int:
        return n << (n & 1)
