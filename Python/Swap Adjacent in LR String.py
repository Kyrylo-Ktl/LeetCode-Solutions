class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    SKIP = 'X'
    LEFT = 'L'
    RIGHT = 'R'

    def canTransform(self, start: str, end: str) -> bool:
        n = len(start)
        i = j = 0

        while i < n or j < n:
            while i < n and start[i] == self.SKIP:
                i += 1

            while j < n and end[j] == self.SKIP:
                j += 1

            if i != j and (i == n or j == n):
                return False

            if i == j == n:
                return True

            if i == n or j == n:
                return False

            if start[i] != end[j]:
                return False

            if start[i] == self.LEFT and i < j:
                return False

            if start[i] == self.RIGHT and i > j:
                return False

            i += 1
            j += 1

        return True
