from typing import List


class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(n)
    """

    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(n*n for n in nums)


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [0] * len(nums)
        left, right = 0, len(nums) - 1

        for i in reversed(range(len(nums))):
            if abs(nums[left]) < abs(nums[right]):
                squares[i] = nums[right]**2
                right -= 1
            else:
                squares[i] = nums[left]**2
                left += 1

        return squares
