from typing import List


class Solution:
    """
    Time:   O(n+m)
    Memory: O(1)
    """

    def merge(self, first: List[int], n: int, second: List[int], m: int) -> None:
        i, j = n - 1, m - 1

        for curr in reversed(range(n + m)):
            if j < 0:
                first[curr] = first[i]
                i -= 1
            elif i < 0:
                first[curr] = second[j]
                j -= 1
            elif first[i] > second[j]:
                first[curr] = first[i]
                i -= 1
            else:
                first[curr] = second[j]
                j -= 1
