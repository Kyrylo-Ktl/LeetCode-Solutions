from typing import List


class Solution:
    """
    Time:   O(n*m)
    Memory: O(1)
    """

    def construct2DArray(self, original: List[int], n: int, m: int) -> List[List[int]]:
        if len(original) != n * m:
            return []
        return [[original[i * m + j] for j in range(m)] for i in range(n)]
