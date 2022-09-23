from functools import reduce


class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(n*log(n))
    """

    MOD = 10 ** 9 + 7

    def concatenatedBinary(self, n: int) -> int:
        return int(''.join(bin(n)[2:] for n in range(1, n + 1)), 2) % self.MOD


class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(1)
    """

    MOD = 10 ** 9 + 7

    def concatenatedBinary(self, n: int) -> int:
        return reduce(lambda x, y: ((x << y.bit_length()) | y) % self.MOD, range(1, n + 1))
