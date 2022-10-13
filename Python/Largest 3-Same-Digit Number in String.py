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


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    K = 3

    def largestGoodInteger(self, num: str) -> str:
        max_good = ''

        for i in range(2, len(num)):
            if num[i - 2] == num[i - 1] == num[i]:
                max_good = max(max_good, num[i])

        return max_good * self.K
