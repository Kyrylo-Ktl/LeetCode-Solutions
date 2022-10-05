from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: 1}
        cum_sum = subarrays = 0

        for num in nums:
            cum_sum += num
            if cum_sum - k in prefix_sum:
                subarrays += prefix_sum[cum_sum - k]
            prefix_sum[cum_sum] = prefix_sum.get(cum_sum, 0) + 1

        return subarrays
