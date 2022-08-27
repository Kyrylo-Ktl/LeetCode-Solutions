from functools import lru_cache
from functools import reduce


class Solution:
    """
    Time:   O(n^2)
    Memory: O(log(n))
    """

    def numTrees(self, n: int) -> int:
        return self._num_trees(1, n)

    @classmethod
    @lru_cache(maxsize=None)
    def _num_trees(cls, lo: int, hi: int) -> int:
        if hi - lo < 1:
            return 1
        return sum(cls._num_trees(lo, i - 1) * cls._num_trees(i + 1, hi) for i in range(lo, hi + 1))


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def numTrees(self, n: int) -> int:
        return reduce(lambda res, i: res * 2 * (2 * i + 1) // (i + 2), range(n), 1)
