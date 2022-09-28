from math import gcd
from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def findGCD(self, nums: List[int]) -> int:
        return gcd(min(nums), max(nums))


class Solution:
    """
    Time:   O(n)
    Memory: O(log(n))
    """

    def findGCD(self, nums: List[int]) -> int:
        return self.gcd(min(nums), max(nums))

    @classmethod
    def gcd(cls, a: int, b: int) -> int:
        return a if not b else cls.gcd(b, a % b)


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def findGCD(self, nums: List[int]) -> int:
        return self.gcd(min(nums), max(nums))

    @staticmethod
    def gcd(a: int, b: int) -> int:
        while a and b:
            a, b = b, a % b
        return a or b
