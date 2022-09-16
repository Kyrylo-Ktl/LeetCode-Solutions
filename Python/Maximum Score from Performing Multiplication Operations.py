from typing import List


class Solution:
    """
    Time:   O(m^2)
    Memory: O(m)
    """

    def maximumScore(self, nums: List[int], mult: List[int]) -> int:
        m = len(mult)
        dp = [0] * (m + 1)

        for i in reversed(range(m)):
            tmp = [0] * (i + 1)
            for l in reversed(range(i + 1)):
                tmp[l] = max(
                    dp[l + 1] + mult[i] * nums[l],
                    dp[l] + mult[i] * nums[~(i - l)],
                )
            dp = tmp

        return dp[0]
