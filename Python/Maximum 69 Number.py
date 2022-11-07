class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def maximum69Number(self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))
