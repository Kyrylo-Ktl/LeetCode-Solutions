from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def canReach(self, arr: List[int], start: int):
        if not (0 <= start < len(arr)) or arr[start] < 0:
            return False
        if arr[start] == 0:
            return True

        arr[start] = -arr[start]
        left_search = self.canReach(arr, start + arr[start])
        right_search = self.canReach(arr, start - arr[start])
        arr[start] = -arr[start]

        return left_search or right_search
