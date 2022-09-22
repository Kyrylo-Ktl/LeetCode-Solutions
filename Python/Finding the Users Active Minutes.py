from collections import defaultdict
from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n + k)
    """

    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        active_minutes = defaultdict(set)

        for user_id, minute in logs:
            active_minutes[user_id].add(minute)

        uam = [0] * k
        for minutes in active_minutes.values():
            uam[len(minutes) - 1] += 1

        return uam
