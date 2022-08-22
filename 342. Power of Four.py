from math import log


class Solution:
    """
    Time:   O(log(n))
    Memory: O(1)
    """

    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and log(n, 4).is_integer()
