class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2
