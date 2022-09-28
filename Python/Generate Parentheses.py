from typing import Generator


class Solution:
    """
    Time:   O(2^n)
    Memory: O(n)
    """

    def generateParenthesis(self, n: int) -> Generator:
        return self._generate(opened=n, closed=n, string='')

    @classmethod
    def _generate(cls, opened: int, closed: int, string: str) -> Generator:
        if opened == closed == 0:
            yield string
        if closed >= opened:
            if opened:
                yield from cls._generate(opened - 1, closed, string + '(')
            if closed:
                yield from cls._generate(opened, closed - 1, string + ')')
