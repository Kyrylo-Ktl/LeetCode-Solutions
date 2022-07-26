import re


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """
    NUMBER_REGEX = r'^[\+\-]?0*\d+'

    def myAtoi(self, s: str) -> int:
        numbers = re.search(self.NUMBER_REGEX, s.strip())

        if numbers is None:
            return 0

        return max(-2 ** 31, min(2 ** 31 - 1, int(numbers.group(0))))
