class Solution:
    """
    Time:   O(log10(n))
    Memory: O(1)
    """

    MAX_BITS = 32

    def hammingWeight(self, n: int) -> int:
        return sum((n >> bit) & 1 for bit in range(self.MAX_BITS))


class Solution:
    """
    Time:   O(log10(n))
    Memory: O(1)
    """

    def hammingWeight(self, n: int) -> int:
        return n.bit_count()
