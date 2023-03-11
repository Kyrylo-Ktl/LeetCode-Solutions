class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def checkZeroOnes(self, string: str) -> bool:
        best_one = best_zero = current_one = current_zero = 0

        for c in string:
            if c == '1':
                current_zero = 0
                current_one += 1
                best_one = max(best_one, current_one)
            else:
                current_zero += 1
                current_one = 0
                best_zero = max(best_zero, current_zero)

        return best_one > best_zero
