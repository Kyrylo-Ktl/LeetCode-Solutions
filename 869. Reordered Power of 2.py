from collections import Counter


class Solution:
    """
    Time:   O(log(n)^2)
    Memory: O(log(n))
    """

    def reorderedPowerOf2(self, n: int) -> bool:
        digits = Counter(str(n))
        return any(digits == Counter(str(1 << power)) for power in range(32))
