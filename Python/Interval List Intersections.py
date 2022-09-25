from typing import List


class Solution:
    """
    Time:   O(n + m)
    Memory: O(n + m)
    """

    def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
        i = j = 0
        intersection = []

        while i < len(first) and j < len(second):
            a_start, a_end = first[i]
            b_start, b_end = second[j]

            start, end = max(a_start, b_start), min(a_end, b_end)
            if start <= end:
                intersection.append([start, end])

            if a_end < b_end:
                i += 1
            else:
                j += 1

        return intersection
