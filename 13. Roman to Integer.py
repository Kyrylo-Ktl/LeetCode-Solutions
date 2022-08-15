class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    ROMAN_TO_INTEGER = {
        'I':  1,
        'IV': 4,
        'V':  5,
        'IX': 9,
        'X':  10,
        'XL': 40,
        'L':  50,
        'XC': 90,
        'C':  100,
        'CD': 400,
        'D':  500,
        'CM': 900,
        'M':  1000,
    }

    def romanToInt(self, s: str) -> int:
        converted = 0

        for roman, integer in self.ROMAN_TO_INTEGER.items():
            while s.endswith(roman):
                s = s.removesuffix(roman)
                converted += integer

        return converted