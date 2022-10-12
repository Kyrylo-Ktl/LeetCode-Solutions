class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    K = 3

    def largestGoodInteger(self, num: str) -> str:
        for d in reversed(range(10)):
            good = str(d) * self.K
            if good in num:
                return good
        return ''
