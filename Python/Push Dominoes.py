class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        force = [0] * n

        f = 0
        for i in range(n):
            if dominoes[i] == 'R':
                f = n
            elif dominoes[i] == 'L':
                f = 0
            else:
                f = max(f - 1, 0)
            force[i] += f

        f = 0
        for i in reversed(range(n)):
            if dominoes[i] == 'L':
                f = n
            elif dominoes[i] == 'R':
                f = 0
            else:
                f = max(f - 1, 0)
            force[i] -= f

        return ''.join('.' if f == 0 else 'R' if f > 0 else 'L' for f in force)


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        force = [0] * n

        f = 0
        for i in range(n):
            f = {
                'L': 0,
                'R': n,
                '.': max(f - 1, 0),
            }[dominoes[i]]
            force[i] += f

        f = 0
        for i in range(n - 1, -1, -1):
            f = {
                'L': n,
                'R': 0,
                '.': max(f - 1, 0),
            }[dominoes[i]]
            force[i] -= f

        return ''.join({
            f == 0: '.',
            f < 0: 'L',
            f > 0: 'R',
        }[True] for f in force)
