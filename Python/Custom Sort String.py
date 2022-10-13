class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(n+m)

    where n - length of s
          m - length of order
    """

    def customSortString(self, order: str, s: str) -> str:
        weight = {c: w for w, c in enumerate(order)}
        return ''.join(sorted(s, key=lambda x: weight.get(x, -1)))
