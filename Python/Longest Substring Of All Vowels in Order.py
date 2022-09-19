class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def longestBeautifulSubstring(self, word: str) -> int:
        longest = 0
        current = 1
        unique = 1

        for i in range(1, len(word)):
            if word[i - 1] > word[i]:
                current = 1
                unique = 1
            elif word[i - 1] < word[i]:
                current += 1
                unique += 1
            else:
                current += 1

            if unique == 5:
                longest = max(longest, current)

        return longest
