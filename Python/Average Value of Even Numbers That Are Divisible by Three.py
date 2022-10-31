from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def averageValue(self, nums: List[int]) -> int:
        divisible_by_three = [num for num in nums if not num % 3 and not num & 1]
        return sum(divisible_by_three) // (len(divisible_by_three) or 1)


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def averageValue(self, nums: List[int]) -> int:
        nums_sum = nums_count = 0

        for num in nums:
            if not num & 1 and not num % 3:
                nums_sum += num
                nums_count += 1

        return nums_sum // (nums_count or 1)
