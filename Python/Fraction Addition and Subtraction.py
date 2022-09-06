import re
from fractions import Fraction


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    FRACTION_PATTERN = r'([+-]?[^+-]+)'

    def fractionAddition(self, expression: str) -> str:
        result_fraction = Fraction(0)

        for exp in re.findall(self.FRACTION_PATTERN, expression):
            n, d = map(int, exp.split('/'))
            result_fraction += Fraction(n, d)

        return f'{result_fraction.numerator}/{result_fraction.denominator}'


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    FRACTION_PATTERN = r'([+-]?[^+-]+)'

    def fractionAddition(self, expression: str) -> str:
        result_fraction = sum(
            (Fraction(*map(int, exp.split('/'))) for exp in re.findall(self.FRACTION_PATTERN, expression)),
            Fraction(0)
        )
        return f'{result_fraction.numerator}/{result_fraction.denominator}'
