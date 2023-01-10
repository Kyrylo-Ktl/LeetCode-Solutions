class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def minimumPartition(self, s: str, k: int) -> int:
        partitions = 1
        num = 0

        for d in map(int, s):
            num = 10 * num + d

            if num > k:
                partitions += 1
                num = d

            if num > k:
                return -1

        return partitions
