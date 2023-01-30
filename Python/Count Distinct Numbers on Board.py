class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    def distinctIntegers(self, n: int) -> int:
        return max(1, n - 1)
