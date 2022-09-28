from math import gcd


class Solution:
    """
    Time:   O(n+m)
    Memory: O(n+m)
    """

    def gcdOfStrings(self, a: str, b: str) -> str:
        n, m = len(a), len(b)
        return '' if a + b != b + a else a[:gcd(n, m)]
