class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
