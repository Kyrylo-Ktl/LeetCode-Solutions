from typing import Generator, List


class Solution:
    """
    Time:   O(2^n)
    Memory: O(n)
    """

    def subsets(self, nums: List[int]) -> Generator:
        return self._subsets_generator(nums, 0, [])

    @classmethod
    def _subsets_generator(cls, nums: List[int], i: int, acc: List[int]) -> Generator:
        if i < len(nums):
            yield from cls._subsets_generator(nums, i + 1, acc + [nums[i]])
            yield from cls._subsets_generator(nums, i + 1, acc)
        else:
            yield acc


class Solution:
    """
    Time:   O(n*2^n)
    Memory: O(1)
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        return [[nums[i] for i in range(n) if (n >> i) & 1] for n in range(1 << n)]
