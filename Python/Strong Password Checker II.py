import re


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    PATTERN = r'(?!.*(.)\1)(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()+-]).{8,}'

    def strongPasswordCheckerII(self, password: str) -> bool:
        return re.fullmatch(self.PATTERN, password) is not None
