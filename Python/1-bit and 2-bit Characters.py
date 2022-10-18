from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i, n = 0, len(bits) - 1

        while i < n:
            i += 2 if bits[i] == 1 else 1

        return i == n
