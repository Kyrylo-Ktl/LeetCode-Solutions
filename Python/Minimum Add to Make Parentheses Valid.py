class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def minAddToMakeValid(self, s: str) -> int:
        score = add = 0

        for ch in s:
            score += -1 if ch == ')' else 1
            if score < 0:
                add += 1
                score = 0

        return score + add
