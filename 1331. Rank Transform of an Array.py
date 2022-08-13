from typing import List


class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(n)
    """

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {num: r for r, num in enumerate(sorted(set(arr)), start=1)}
        return [ranks[num] for num in arr]
