from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        best_id = best_time = start = 0

        for emp_id, end in logs:
            time = end - start
            if time > best_time or (time == best_time and best_id > emp_id):
                best_id = emp_id
                best_time = time
            start = end

        return best_id
