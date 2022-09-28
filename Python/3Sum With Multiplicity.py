from collections import Counter
from typing import List


class Solution:
    """
    Time:   O(k^2)
    Memory: O(k)

    where k - number of unique numbers
    """

    MOD = 10 ** 9 + 7

    def threeSumMulti(self, nums: List[int], target: int) -> int:
        count = Counter(nums)
        nums = sorted(count.keys())
        triples = 0

        for i, x in enumerate(nums):
            x = nums[i]
            j, k = i, len(nums) - 1

            while j <= k:
                y = nums[j]
                z = nums[k]

                s = x + y + z
                if s < target:
                    j += 1
                elif s > target:
                    k -= 1
                else:
                    if i < j < k:
                        triples += count[x] * count[y] * count[z]
                    elif i == j < k:
                        triples += count[x] * (count[x] - 1) // 2 * count[z]
                    elif i < j == k:
                        triples += count[x] * count[y] * (count[y] - 1) // 2
                    else:
                        triples += count[x] * (count[x] - 1) * (count[x] - 2) // 6
                    j += 1
                    k -= 1

        return triples % self.MOD
