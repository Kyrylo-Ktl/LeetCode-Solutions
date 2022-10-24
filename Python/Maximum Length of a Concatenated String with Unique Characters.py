from typing import List


class Solution:
    """
    Time:   O(n^2)
    Memory: O(n^2)
    """

    def maxLength(self, sequences: List[str]) -> int:
        dp = [set()]

        for seq in sequences:
            chars = set(seq)

            if len(chars) < len(seq):
                continue

            dp.extend(chars | other for other in dp if not (chars & other))

        return max(map(len, dp))
