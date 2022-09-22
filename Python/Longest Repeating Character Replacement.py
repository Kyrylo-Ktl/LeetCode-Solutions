from collections import defaultdict


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        max_freq = max_len = i = 0

        for j in range(len(s)):
            freq[s[j]] += 1
            max_freq = max(max_freq, freq[s[j]])

            if (j - i + 1) - max_freq > k:
                freq[s[i]] -= 1
                i += 1
            else:
                max_len = max(max_len, j - i + 1)

        return max_len
