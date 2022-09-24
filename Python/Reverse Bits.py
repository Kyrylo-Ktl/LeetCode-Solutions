class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    MAS_BITS = 32

    def reverseBits(self, n: int) -> int:
        return sum(1 << (self.MAS_BITS - 1 - bit) for bit in range(self.MAS_BITS) if (n >> bit) & 1)


class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    def reverseBits(self, n: int) -> int:
        n = ((n & 0x55555555) << 1) | ((n & 0xAAAAAAAA) >> 1)
        n = ((n & 0x33333333) << 2) | ((n & 0xCCCCCCCC) >> 2)
        n = ((n & 0x0F0F0F0F) << 4) | ((n & 0xF0F0F0F0) >> 4)
        n = ((n & 0x00FF00FF) << 8) | ((n & 0xFF00FF00) >> 8)
        n = ((n & 0x0000FFFF) << 16) | ((n & 0xFFFF0000) >> 16)
        return n
