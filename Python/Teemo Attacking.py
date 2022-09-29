from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def findPoisonedDuration(self, time_series: List[int], duration: int) -> int:
        poisoned_util = -1
        total_duration = 0

        for time in time_series:
            total_duration += duration
            if poisoned_util >= time:
                total_duration -= poisoned_util - time + 1
            poisoned_util = time + duration - 1

        return total_duration


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def findPoisonedDuration(self, time_series: List[int], duration: int) -> int:
        if not time_series:
            return 0
        return sum(
            min(time_series[i + 1] - time_series[i], duration)
            for i in range(len(time_series) - 1)
        ) + duration
