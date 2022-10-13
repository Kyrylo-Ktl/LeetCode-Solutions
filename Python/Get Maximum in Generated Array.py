class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def getMaximumGenerated(self, n: int) -> int:
        nums = [0, 1] + [0] * n

        for i in range(n + 1):
            nums[i] = nums[i // 2] + nums[i // 2 + 1] * (i & 1)

        return max(nums[:-1])
