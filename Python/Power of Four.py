from math import log


class Solution:
    """
    Time:   O(log(n))
    Memory: O(1)
    """

    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and log(n, 4).is_integer()


class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    POWERS = {4 ** n for n in range(16)}

    def isPowerOfFour(self, n: int) -> bool:
        return n in self.POWERS
