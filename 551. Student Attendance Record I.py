class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def checkRecord(self, s: str) -> bool:
        return s.count('A') < 2 and 'LLL' not in s
