from typing import List


class Solution:
    """
    Time:   O(2^n)
    Memory: O(1)
    """

    def grayCode(self, n: int) -> List[int]:
        return [i ^ (i >> 1) for i in range(1 << n)]
