from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = k

        for bit in nums:
            if bit:
                if count < k:
                    return False
                count = 0
            else:
                count += 1

        return True
