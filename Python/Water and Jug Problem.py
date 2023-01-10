from math import gcd


class Solution:
    """
    Time:   O(log2(max(n,m)))
    Memory: O(log2(max(n,m)))

    where n - first_jug,
          m - second_jug
    """

    def canMeasureWater(self, first_jug: int, second_jug: int, target: int) -> bool:
        if first_jug + second_jug < target:
            return False
        if first_jug == target or second_jug == target:
            return True
        return not target % gcd(first_jug, second_jug)
