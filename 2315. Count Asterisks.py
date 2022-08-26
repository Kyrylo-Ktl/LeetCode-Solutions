class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def countAsterisks(self, s: str) -> int:
        is_closed = True
        count = 0

        for c in s:
            count += is_closed * c == '*'
            is_closed ^= c == '|'

        return count
