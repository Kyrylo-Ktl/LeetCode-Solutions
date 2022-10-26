from math import gcd
from typing import List


class Solution:
    """
    Time:   O(n^2*log(m))
    Memory: O(1)

    where m - maximum number in nums
    """

    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sub_arrays = 0

        for i in range(n):
            curr_gcd = 0
            for j in range(i, n):
                curr_gcd = gcd(curr_gcd, nums[j])

                if curr_gcd == k:
                    sub_arrays += 1
                elif curr_gcd < k:
                    break

        return sub_arrays
