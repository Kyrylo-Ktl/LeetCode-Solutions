class Solution:
    """
    Time:   O(min(n,m))
    Memory: O(1)
    """

    def commonFactors(self, n: int, m: int) -> int:
        return sum(not (n % i or m % i) for i in range(1, min(n, m) + 1))
