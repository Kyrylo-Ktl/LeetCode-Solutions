from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def maxScore(self, cards: List[int], k: int) -> int:
        n = len(cards)
        size = n - k
        min_window = window = sum(cards[:size])

        for i in range(size, n):
            window += cards[i] - cards[i - size]
            min_window = min(min_window, window)

        return sum(cards) - min_window
