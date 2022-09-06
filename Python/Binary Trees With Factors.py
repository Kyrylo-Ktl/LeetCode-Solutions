from typing import List


class Solution:
    """
    Time:   O(n^2)
    Memory: O(n)
    """

    MOD = 1000000007

    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dp = {x: 1 for x in arr}

        for i in range(len(arr)):
            for j in range(i):
                if arr[i] / arr[j] in dp:
                    dp[arr[i]] += dp[arr[j]] * dp[arr[i] / arr[j]]

        return sum(dp.values()) % self.MOD
