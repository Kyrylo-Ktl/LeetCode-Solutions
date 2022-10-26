from itertools import cycle


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    OPERATIONS = ('*', '//', '+', '-')

    def clumsy(self, n: int) -> int:
        op = cycle(self.OPERATIONS)
        return eval(''.join(f'{n}{next(op)}' for n in range(n, 1, -1)) + '1')


class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    def clumsy(self, n: int) -> int:
        if n <= 2:
            return n
        if n <= 4:
            return n + 3
        if (n - 4) % 4 == 0:
            return n + 1
        if (n - 4) % 4 <= 2:
            return n + 2
        return n - 1
