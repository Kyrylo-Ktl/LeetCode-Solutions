class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def convert(self, string: str, n_rows: int) -> str:
        if n_rows == 1:
            return string

        rows = [''] * n_rows
        turn = -1
        curr_level = 0

        for i, c in enumerate(string):
            if not i % (n_rows - 1):
                turn *= -1
            rows[curr_level] += c
            curr_level += turn

        return ''.join(rows)
