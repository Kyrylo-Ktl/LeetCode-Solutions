class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0
