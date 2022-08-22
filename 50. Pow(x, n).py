class Solution:
    """
    Time:   O(log(n))
    Memory: O(1)
    """

    def myPow(self, x: int, n: int) -> float:
        return x ** n


class Solution:
    """
    Time:   O(log(n))
    Memory: O(log(n))
    """

    def myPow(self, x: int, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            return 1 / self.myPow(x, -n)

        if n & 1:
            return x * self.myPow(x, n - 1)

        return self.myPow(x * x, n // 2)
