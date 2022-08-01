class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    ROMAN_TO_INTEGER = {
        'M':  1000,
        'CM': 900,
        'D':  500,
        'CD': 400,
        'C':  100,
        'XC': 90,
        'L':  50,
        'XL': 40,
        'X':  10,
        'IX': 9,
        'V':  5,
        'IV': 4,
        'I':  1,
    }

    def intToRoman(self, num: int) -> str:
        converted = ''

        for roman, integer in self.ROMAN_TO_INTEGER.items():
            whole, num = divmod(num, integer)
            converted += whole * roman

        return converted
