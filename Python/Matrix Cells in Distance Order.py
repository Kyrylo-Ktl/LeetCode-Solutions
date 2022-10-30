from typing import List


class Solution:
    """
    Time:   O(n*m*log(n*m))
    Memory: O(1)
    """

    def allCellsDistOrder(self, rows: int, cols: int, r_center: int, c_center: int) -> List[List[int]]:
        return sorted(
            [[r, c] for r in range(rows) for c in range(cols)],
            key=lambda x: abs(x[0] - r_center) + abs(x[1] - c_center),
        )
