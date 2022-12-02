from math import sqrt


class Solution:
    """
    Time:   O(√n)
    Memory: O(1)
    """

    def pivotInteger(self, n: int) -> int:
        m = sqrt(n * (n + 1) / 2)
        return int(m) if m.is_integer() else -1
