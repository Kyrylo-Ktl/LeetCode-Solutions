class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def partitionString(self, s: str) -> int:
        used = set()
        partitions = 0

        for c in s:
            if c in used:
                used.clear()
                partitions += 1
            used.add(c)

        return partitions + 1


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    MIN_CHAR = 'a'

    def partitionString(self, s: str) -> int:
        used = 0
        partitions = 0

        for c in s:
            bit = 1 << ord(c) - ord(self.MIN_CHAR)
            if used & bit != 0:
                used = 0
                partitions += 1
            used |= bit

        return partitions + 1
