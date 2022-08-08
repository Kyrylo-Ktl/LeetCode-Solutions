class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(log(n))
    """

    SINGLE = {'0', '1', '8'}
    PAIRED = {'2', '5', '6', '9'}
    ROTATABLE = SINGLE | PAIRED

    def rotatedDigits(self, n: int) -> int:
        return sum(map(self.is_good, range(n + 1)))

    @classmethod
    def is_good(cls, num: int) -> bool:
        digits = set(str(num))
        return digits.issubset(cls.ROTATABLE) and not digits.issubset(cls.SINGLE)
