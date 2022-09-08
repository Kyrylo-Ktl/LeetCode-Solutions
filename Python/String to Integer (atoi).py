import re


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    NUMBER_REGEX = r'^[\+\-]?0*\d+'
    MAX_NUM = (1 << 31) - 1
    MIN_NUM = -(1 << 31)

    def myAtoi(self, s: str) -> int:
        numbers = re.search(self.NUMBER_REGEX, s.strip())
        num = 0 if numbers is None else int(numbers.group(0))
        return max(self.MIN_NUM, min(self.MAX_NUM, num))
