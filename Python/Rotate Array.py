from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def rotate(self, nums: List[int], k: int):
        k %= len(nums)
        for i, num in enumerate(nums[-k:] + nums[:-k]):
            nums[i] = num


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def rotate(self, nums: List[int], k: int):
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    @staticmethod
    def reverse(nums: List[int], l: int, r: int):
        for i in range((r - l) // 2 + 1):
            nums[l + i], nums[r - i] = nums[r - i], nums[l + i]
