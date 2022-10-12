class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    MOVES = {
        'N': lambda x, y: (x, y + 1),
        'S': lambda x, y: (x, y - 1),
        'E': lambda x, y: (x + 1, y),
        'W': lambda x, y: (x - 1, y),
    }

    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        seen = {(x, y)}

        for move in path:
            x, y = self.MOVES[move](x, y)
            if (x, y) in seen:
                return True
            seen.add((x, y))

        return False
