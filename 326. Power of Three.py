class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    def isPowerOfThree(self, num: int) -> bool:
        return num > 0 and not 1162261467 % num
