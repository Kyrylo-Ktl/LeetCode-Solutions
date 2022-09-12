class Solution:
    """
    Time:   O(log(k))
    Memory: O(log(k))
    """

    def findMinFibonacciNumbers(self, k: int) -> int:
        if k < 2:
            return k
        return self.findMinFibonacciNumbers(k - self.min_fib(k)) + 1

    @staticmethod
    def min_fib(n: int) -> int:
        a, b = 1, 1
        while b <= n:
            a, b = b, a + b
        return a
