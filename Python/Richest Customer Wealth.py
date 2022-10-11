from typing import List


class Solution:
    """
    Time:   O(n*m)
    Memory: O(1)
    """

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))
