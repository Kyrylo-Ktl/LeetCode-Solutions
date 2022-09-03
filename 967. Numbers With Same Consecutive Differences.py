from typing import Generator, List


class Solution:
    """
    Time:   O(2^n)
    Memory: O(2^n)
    """

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [i for i in range(10)]
        return [num for digit in range(1, 10) for num in self.dfs(n - 1, k, digit)]

    @classmethod
    def dfs(cls, digits: int, diff: int, num: int) -> Generator:
        if digits == 0:
            yield num
        else:
            last_digit = num % 10
            for digit in {last_digit + diff, last_digit - diff}:
                if 0 <= digit < 10:
                    yield from cls.dfs(digits - 1, diff, num * 10 + digit)


class Solution:
    """
    Time:   O(2^n)
    Memory: O(2^n)
    """

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        nums = list(range(1, 10))

        for i in range(1, n):
            nums = [num * 10 + d for num in nums for d in {num % 10 + k, num % 10 - k} if 0 <= d <= 9]

        return nums

