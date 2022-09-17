from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def minGroups(self, intervals: List[List[int]]) -> int:
        schedule = []
        for start, end in intervals:
            schedule.append([start, 1])
            schedule.append([end + 1, -1])

        min_groups = groups = 0
        for _, diff in sorted(schedule):
            groups += diff
            min_groups = max(min_groups, groups)

        return min_groups
