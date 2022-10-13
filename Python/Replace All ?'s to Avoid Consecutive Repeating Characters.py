from string import ascii_lowercase


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    REPLACEABLE = '?'

    def modifyString(self, s: str) -> str:
        s = list('#' + s + '#')

        for i, c in enumerate(s):
            if c == self.REPLACEABLE:
                s[i] = next(x for x in ascii_lowercase if s[i - 1] != x != s[i + 1])

        return ''.join(s[1:-1])
