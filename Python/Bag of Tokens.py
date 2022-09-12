from typing import List


class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(1)
    """

    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i, j = 0, len(tokens) - 1
        max_score = score = 0

        while i <= j:
            if tokens[i] <= power:
                power -= tokens[i]
                score += 1
                i += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[j]
                score -= 1
                j -= 1
            else:
                break

        return max_score
