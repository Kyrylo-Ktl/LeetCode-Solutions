class Solution:
    """
    Time:   O(log(n))
    Memory: O(1)
    """

    def isUgly(self, n: int) -> bool:
        while n > 1:
            if not n % 5:
                n //= 5
            elif not n % 3:
                n //= 3
            elif not n % 2:
                n //= 2
            else:
                return False

        return n > 0
