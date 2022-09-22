from collections import Counter


class Solution:
    """
    Time:   O(n)
    Memory: O(min(k, n))
    """

    K = 3

    def countGoodSubstrings(self, s: str) -> int:
        window = Counter(s[:self.K])
        count = int(len(window) == self.K)

        for i in range(self.K, len(s)):
            if window[s[i - self.K]] > 1:
                window[s[i - self.K]] -= 1
            else:
                window.pop(s[i - self.K])
            window[s[i]] += 1

            count += int(len(window) == self.K)

        return count
