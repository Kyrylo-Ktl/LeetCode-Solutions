from typing import List


class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    WIN_MASKS = {7, 56, 73, 84, 146, 273, 292, 448}

    def tictactoe(self, moves: List[List[int]]) -> str:
        cross_mask = zero_mask = 0

        for ind, (r, c) in enumerate(moves):
            if ind & 1:
                zero_mask |= 1 << 3 * r + c
            else:
                cross_mask |= 1 << 3 * r + c

        for mask in self.WIN_MASKS:
            if mask & cross_mask == mask:
                return 'A'
            if mask & zero_mask == mask:
                return 'B'

        return "Draw" if len(moves) == 9 else "Pending"
