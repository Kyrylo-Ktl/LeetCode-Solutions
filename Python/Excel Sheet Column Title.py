from string import ascii_uppercase


class Solution:
    """
    Time:   O(log26(n))
    Memory: O(1)
    """

    def convertToTitle(self, column_num: int) -> str:
        title = ''

        while column_num:
            column_num, ltr = divmod(column_num - 1, 26)
            title = ascii_uppercase[ltr] + title

        return title
