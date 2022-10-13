class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def checkOnesSegment(self, s: str) -> bool:
        return '01' not in s
