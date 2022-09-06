from typing import List


class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(1)
    """

    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        left, right = 0, len(nums) - 1

        for j, num in enumerate(nums):
            if self.binary_search(nums, num - diff, left, j - 1) != -1 and \
               self.binary_search(nums, num + diff, j + 1, right) != -1:
                count += 1

        return count

    @staticmethod
    def binary_search(nums: List[int], target: int, left: int, right: int) -> int:
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        uniq_nums = set(nums)
        return sum(num + diff in uniq_nums and num + 2 * diff in uniq_nums for num in nums)
