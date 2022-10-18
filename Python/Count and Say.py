from itertools import groupby


class Solution:
    """
    Time:   O(2^n)
    Memory: O(2^n)
    """

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        return self.make_count(self.countAndSay(n - 1))

    @staticmethod
    def make_count(n: str) -> str:
        return ''.join(f'{sum(1 for _ in gr)}{key}' for key, gr in groupby(n))


class Solution:
    """
    Time:   O(2^n)
    Memory: O(2^n)
    """

    def countAndSay(self, n: int) -> str:
        string = '1'

        for _ in range(n - 1):
            string = self.make_count(string)

        return string

    @staticmethod
    def make_count(n: str) -> str:
        return ''.join(f'{sum(1 for _ in gr)}{key}' for key, gr in groupby(n))
